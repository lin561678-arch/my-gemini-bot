import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import google.generativeai as genai

# --- Settings ---
# Bot Token အသစ်ကို ဒီမှာ ထည့်ထားပါတယ်
TELEGRAM_TOKEN = "8144493236:AAFvqX1zMcYl4aXNaAEOUhCpIEMFsJ5G87U"
GEMINI_KEY = "AIzaSyBGqOjEgiip8pTqJeVS0_cyz1JLWoItCEE"

# Gemini Config
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('models/gemini-1.5-flash')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
    user_text = update.message.text
    try:
        response = model.generate_content(user_text)
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("New Bot is starting...")
    application.run_polling(drop_pending_updates=True)
  
