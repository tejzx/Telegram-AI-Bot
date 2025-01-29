from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import google.generativeai as genai
from pymongo import MongoClient
import os

# Set your credentials
TOKEN = "7690009681:AAEocekOnYcjVPFMYTHfHLZwZaRy87kP7Nc"
API_KEY = "AIzaSyACBHqiPlPkxVlKDcjQrViteS894BXlYiA"
MONGO_URI = "mongodb+srv://reachteju10:CnFvbuFYN5rTF5SP@cluster0.sisk6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "Cluster0"

# Configure the generative model
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
vision_model = genai.GenerativeModel('gemini-pro-vision')

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
users_collection = db["users"]
chats_collection = db["chats"]

# Function to generate text response
def generate_content(full_prompt: str) -> str:
    try:
        response = model.generate_content(full_prompt)
        return response.text if hasattr(response, 'text') else "Sorry, I couldn't generate a response."
    except Exception as e:
        return f"There was an error generating the response: {str(e)}"

# Function to generate an image
def generate_image(prompt: str):
    try:
        response = vision_model.generate_content(prompt)
        if response and hasattr(response, 'text'):
            return response.text  # Modify this part if API supports image response differently
        return "Sorry, I couldn't generate an image."
    except Exception as e:
        return f"There was an error generating the image: {str(e)}"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    user_data = {
        "user_id": user.id,
        "first_name": user.first_name,
        "username": user.username,
    }
    
    users_collection.update_one({"user_id": user.id}, {"$set": user_data}, upsert=True)
    system_message = f"Hello {user.first_name}! I am a chatbot. How can I help you today?"
    await update.message.reply_text(system_message)

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    user_id = update.effective_user.id
    
    if user_message.startswith("/image"):
        prompt = user_message.replace("/image", "").strip()
        if not prompt:
            await update.message.reply_text("Please provide a prompt for image generation.")
            return
        response_text = generate_image(prompt)
    else:
        response_text = generate_content(user_message)
    
    # Store chat in MongoDB
    chat_data = {
        "user_id": user_id,
        "message": user_message,
        "response": response_text
    }
    chats_collection.insert_one(chat_data)
    
    await update.message.reply_text(response_text)

# Build the application
app = ApplicationBuilder().token(TOKEN).build()

# Add handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

# Run the bot
app.run_polling()