import os
# bot.py
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# ===== Hardcode your Telegram Bot Token here =====
TELEGRAM_BOT_TOKEN = "8079637279:AAGaW8-dcWInsP0BgFxjbdDEfyxYRPjtE_o"

def start(update, context):
    update.message.reply_text("🎵 K Music Bot is running!")

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Command handler
    dp.add_handler(CommandHandler("start", start))

    # You can add more handlers here
    # Example: echo message
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, lambda u,c: u.message.reply_text("Message received!")))

    # Start polling
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
