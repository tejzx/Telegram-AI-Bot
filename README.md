# Telegram AI Chatbot - TeleAIBot

## Overview
This is a Telegram chatbot powered by Google's Gemini AI for text and image generation. It uses the `python-telegram-bot` library to interact with Telegram users, and MongoDB to store user interactions.

## Features
- Handles text-based conversations using **Gemini-1.5-Flash**.
- Generates AI-powered images using **Gemini-Pro-Vision**.
- Stores user details and chat history in **MongoDB**.
- Supports `/start` command for user onboarding.
- `/image` command for AI-based image generation.

## Tech Stack
- **Python**: Primary programming language.
- **Telegram Bot API**: Handles message interactions.
- **Google Gemini AI**:
  - `gemini-1.5-flash`: For text generation.
  - `gemini-pro-vision`: For image generation.
- **MongoDB**: Stores user details and chat history.
- **PyMongo**: Connects Python to MongoDB.
- **python-telegram-bot**: Manages Telegram bot functionality.

## Setup & Installation
### Prerequisites
- Python 3.8+
- Telegram bot token
- Google Gemini AI API key
- MongoDB instance

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/telegram-gemini-bot.git
   cd telegram-gemini-bot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   ```bash
   export TOKEN="your-telegram-bot-token"
   export API_KEY="your-google-api-key"
   export MONGO_URI="your-mongodb-uri"
   ```
4. Run the bot:
   ```bash
   python bot.py
   ```

## Usage
- Start the bot with `/start`.
- Send any text message to get an AI-generated response.
- Use `/image <prompt>` to generate an image.

## License
This project is licensed under the MIT License.

## Contributing
Feel free to submit issues or pull requests to improve this bot!

## Contact
For any queries, reach out to [reachteju10@example.com](mailto:your-email@example.com).

