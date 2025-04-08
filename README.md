AI NewsBot

Welcome to **AI NewsBot**, a content recommender chatbot built with Flask and powered by AI to fetch and summarize trending news based on user input. This project leverages the NewsAPI for real-time news data and Google Gemini for intelligent summarization, delivering concise bullet points with detailed descriptions.

Features
- Interactive Chat Interface: Users can input topics (e.g., "AI", "sports") to get news summaries.
- AI-Powered Summaries: Utilizes Google Gemini to generate bullet-point summaries with 3-4 line descriptions.
- Real-Time News: Fetches the latest headlines using NewsAPI.
- User-Friendly UI: Dark-themed, responsive design with a sidebar for new chats.
- Welcome Message: Greets users with "I am a Content Recommender Chat-Bot" on startup.

Technologies Used
- Backend: Python, Flask
- AI: Google Generative AI (Gemini)
- API: NewsAPI
- Frontend: HTML, Tailwind CSS
- Deployment: Vercel (serverless)

Prerequisites
- Python 3.7+
- Node.js and npm (for Vercel CLI)
- Git
- API Keys:
  - NewsAPI Key
  - Google Gemini API Key

Installation

Local Setup
1. Clone the Repository:
   git clone https://github.com/your-username/ai-newsbot.git
   cd ai-newsbot

2. Install Dependencies:
   - Create a requirements.txt if not present:
     pip freeze > requirements.txt
   - Install Python packages:
     pip install -r requirements.txt

3. Set Environment Variables:
   - Create a .env file in the root directory:
     NEWS_API_KEY=your_news_api_key
     GEMINI_API_KEY=your_gemini_api_key
   - Alternatively, set them in your shell:
     export NEWS_API_KEY=your_news_api_key
     export GEMINI_API_KEY=your_gemini_api_key

4. Run Locally:
   - Start the Flask app:
     python app.py
   - Open http://localhost:5000 in your browser to test.

Deployment on Vercel
This project is deployed on Vercel using a serverless function approach. Follow these steps:

1. Prepare the Project:
   - Ensure app.py, templates/index.html, static/style.css, requirements.txt, and vercel.json are in your repository.
   - Update app.py with the serverless handler as provided in the deployment guide.

2. Install Vercel CLI:
   npm install -g vercel

3. Log In:
   vercel login

4. Deploy:
   - Navigate to your project directory:
     cd ai-newsbot
   - Deploy with:
     vercel
   - Follow the prompts to configure the project.

5. Set Environment Variables on Vercel:
   - In the Vercel dashboard, go to Settings > Environment Variables.
   - Add NEWS_API_KEY and GEMINI_API_KEY.

6. Access the App:
   - Vercel will provide a URL (e.g., https://ai-newsbot.vercel.app). Test it in your browser.

Usage
- Start a New Chat: Click the "+ New Chat" button to reset the conversation.
- Enter a Topic: Type a topic (e.g., "AI") and click the send button (➤).
- View Response: The bot displays your input, followed by bullet points with 3-4 line descriptions.

File Structure
ai-newsbot/
|-- app.py              # Flask application
|-- templates/          # HTML templates
|   |-- index.html      # Main chat interface
|-- static/             # Static files
|   |-- style.css       # Custom CSS
|-- requirements.txt    # Python dependencies
|-- vercel.json         # Vercel configuration
|-- README.txt          # This file

Contributing
Feel free to fork this repository and submit pull requests. Please open an issue for bugs or feature requests.

License
This project is licensed under the MIT License - see the LICENSE file for details (add a LICENSE file if desired).

Acknowledgements
- NewsAPI (https://newsapi.org) for news data.
- Google Generative AI (https://ai.google.dev/gemini-api) for summarization.
- Vercel (https://vercel.com) for hosting.
- Tailwind CSS (https://tailwindcss.com) for styling.

Contact
For questions or support, reach out to the developer:
- GitHub: your-username (https://github.com/your-username)
- Email: your-email@example.com (replace with your contact)
