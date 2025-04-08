from flask import Flask, render_template, request, jsonify
import requests
import google.generativeai as genai

app = Flask(__name__)

# Load your API  (use environment variables for security)
import os
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "9fe3b81a5b4e42fd81bb0bc9aa10515e")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyCO0XnJzF02ZCGzUejTAjazCDWpbE6tjog")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def fetch_news_from_newsapi(topic):
    query = "artificial+intelligence" if topic.lower() == "ai" else topic
    url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&language=en&pageSize=5&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    articles = data.get("articles", [])
    headlines = [f"{a['title']} - {a['source']['name']}" for a in articles if a.get("title")]
    return headlines

def summarize_with_gemini(topic, headlines):
    news_text = "\n".join([f"- {headline}" for headline in headlines])
    prompt = (
        f"Summarize the following news headlines about '{topic}' into concise bullet points. "
        f"Output exactly one bullet point (➤) per line, with each summary point on a new line. "
        f"After each bullet point, provide a detailed description of 3-4 lines explaining the point. "
        f"Do not include any introductory text, explanations, or paragraphs outside the bullet points and descriptions—just the structured content:\n\n{news_text}"
    )
    response = model.generate_content(prompt)
    lines = response.text.strip().split('\n')
    formatted_response = []
    current_point = None
    for line in lines:
        line = line.strip()
        if line.startswith('➤'):
            if current_point:
                formatted_response.append(current_point)
            current_point = line
        elif current_point and line:
            current_point += '\n' + line
    if current_point:
        formatted_response.append(current_point)
    return '\n'.join(formatted_response)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/get_news', methods=["POST"])
def get_news():
    user_input = request.json.get("message", "").strip()

    if not user_input:
        return jsonify({"reply": "❗ Please enter a topic like 'sports', 'AI', or 'Elon Musk'."})

    try:
        headlines = fetch_news_from_newsapi(user_input)
        if not headlines:
            return jsonify({"reply": "⚠️ No trending news found for that topic."})

        summary = summarize_with_gemini(user_input, headlines)
        return jsonify({"reply": summary})

    except Exception as e:
        print(f"[ERROR]: {str(e)}")
        return jsonify({"reply": "❌ Something went wrong while fetching or summarizing the news."})

# Vercel serverless function handler
def handler(request):
    from werkzeug.middleware.proxy_fix import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)
    from werkzeug.serving import run_simple
    from io import StringIO

    # Simulate WSGI environment
    if request.method == 'GET':
        return app.full_dispatch_request().get_data(as_text=True)
    elif request.method == 'POST':
        return app.full_dispatch_request().get_data(as_text=True)

if __name__ == "__main__":
    app.run(debug=True)