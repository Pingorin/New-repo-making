# bot.py
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# info.py से टोकन इम्पोर्ट करें
from info import BOT_TOKEN

# /start कमांड के लिए फंक्शन
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """जब /start कमांड दिया जाता है तो यह एक संदेश भेजता है।"""
    user = update.effective_user
    await update.message.reply_html(
        f"Hi {user.mention_html()}!",
        reply_markup=None
    )
    # आपका अनुरोधित संदेश भेजें
    await update.message.reply_text("me start ho gya")

def main() -> None:
    """Bot को चलाएं।"""
    # Application बनाएं और अपना टोकन पास करें
    application = Application.builder().token(BOT_TOKEN).build()

    # /start कमांड के लिए एक हैंडलर जोड़ें
    application.add_handler(CommandHandler("start", start))

    # Bot को तब तक चलाएं जब तक आप इसे रोक न दें (Ctrl-C)
    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
  
