import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import logging

TOKEN = "7637175756:AAF6D5YA8dOX-xBr-xfnuQAPOe2RcuJs3ng"
CHANNEL_USERNAME = "@ictwithme"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("✅ عضویت در کانال", url=f"https://t.me/{CHANNEL_USERNAME[1:]}")],
        [InlineKeyboardButton("📥 دریافت خبر", callback_data="get_news")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("👋 به ربات اخبار اقتصادی خوش آمدید.", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "get_news":
        await query.edit_message_text("📨 دریافت اخبار فعال شد. به زودی اخبار را دریافت خواهید کرد.")

async def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
