# Telegram Chatbot Powered by Gemini AI

## Overview
This project is a **Telegram chatbot** powered by **Google's Gemini AI**, allowing users to interact with an intelligent assistant directly through Telegram. The bot can process text queries and respond with AI-generated answers.

## Features
- **AI-powered responses**: Uses Gemini AI for intelligent query processing.
- **Seamless Telegram integration**: Communicates with users via Telegram's bot API.
- **User-friendly interaction**: Simple and intuitive command-based conversation.
- **Scalable and efficient**: Built with Python and can be deployed on cloud platforms.
- **MongoDB Integration**: Stores user interactions and chat history.

## Technologies Used
- **Python**
- **Telegram Bot API**
- **Google Gemini API**
- **Python-Telegram-Bot Library**
- **MongoDB (via PyMongo)**

## Setup Instructions

### 1. Clone the Repository
```sh
 git clone https://github.com/yourusername/telegram-gemini-bot.git
 cd telegram-gemini-bot
```

### 2. Install Dependencies
```sh
pip install python-telegram-bot google-generative-ai python-dotenv pymongo
```

### 3. Get API Keys
- **Telegram Bot API**: Register a bot using [BotFather](https://t.me/botfather) and obtain an API token.
- **Gemini AI API**: Sign up at [Google AI](https://ai.google.dev) and get an API key.
- **MongoDB**: Set up a free cluster at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) and get a connection URI.

### 4. Configure Environment Variables
Create a `.env` file and add the following:
```env
TELEGRAM_BOT_TOKEN='your-telegram-bot-token'
GEMINI_API_KEY='your-gemini-api-key'
MONGO_URI='your-mongodb-connection-uri'
DB_NAME='your-database-name'
```

### 5. Update the Code for MongoDB Integration
Modify `bot.py` to include MongoDB connection:
```python
from pymongo import MongoClient
import os

# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]
users_collection = db["users"]
chats_collection = db["chats"]

# Function to save user info
def save_user(user_id, username):
    users_collection.update_one(
        {"user_id": user_id},
        {"$set": {"username": username}},
        upsert=True
    )

# Function to store chat history
def save_chat(user_id, message, response):
    chats_collection.insert_one({
        "user_id": user_id,
        "message": message,
        "response": response
    })
```

### 6. Run the Bot
```sh
python bot.py
```

## Usage
1. Start the bot by running `/start` in Telegram.
2. Type any query, and the bot will generate responses using Gemini AI.
3. The bot stores user interactions and chat history in MongoDB.

## Deployment
For cloud deployment, use platforms like:
- **Heroku**
- **AWS Lambda**
- **Google Cloud Functions**

## Contributions
Feel free to fork the repository, create issues, or submit pull requests!

## License
This project is open-source and available under the MIT License.
