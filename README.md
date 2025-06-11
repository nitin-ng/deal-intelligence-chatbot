# Deal Intelligence Chatbot 📊

An AI-powered chatbot that analyzes sales opportunity data and provides quick insights for sales reps before client calls.

## Features

- 🤖 **AI-Powered Analysis**: Uses OpenAI GPT-4o-mini for intelligent responses
- 📄 **Auto-loads Analysis**: Automatically reads from `markdown.md` file
- 💬 **Conversational Interface**: Natural language Q&A about deals
- 🔒 **Secure**: Environment variable support for API keys
- ⚡ **Fast Insights**: Get quick answers about deal value, stakeholders, risks, and next steps

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/nitin-ng/deal-intelligence-chatbot.git
   cd deal-intelligence-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```
   OPENAI_API_KEY=your-openai-api-key-here
   ```

4. **Add your analysis file**
   Create a `markdown.md` file with your opportunity analysis content.

5. **Run the app**
   ```bash
   streamlit run chatbot.py
   ```

## Deployment

This app is designed to be deployed on Streamlit Community Cloud:

1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select this repository
5. Set `chatbot.py` as the main file
6. Add your `OPENAI_API_KEY` in the secrets section
7. Deploy!

## Usage

1. The app automatically loads your `markdown.md` analysis file
2. Ask questions about your opportunity in natural language
3. Get instant insights about deal value, stakeholders, risks, and next steps
4. Perfect for prep before client calls!

## Example Questions

- "What's the deal value?"
- "Who is the economic buyer?"
- "What are the main risks?"
- "What are the next steps?"
- "Who are the champions?"

## Tech Stack

- **Frontend**: Streamlit
- **AI**: OpenAI GPT-4o-mini
- **Language**: Python
- **Deployment**: Streamlit Community Cloud 