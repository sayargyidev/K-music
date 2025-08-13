import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

# Get Telegram bot token from environment variable
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def start(update, context):
    update.message.reply_text("🎵 Send me a song name and I'll find it for you!")

def search_song(update, context):
    query = update.message.text.strip()
    if not query:
        update.message.reply_text("Please type a song name.")
        return

    # Search via iTunes API (supports Myanmar + worldwide)
    url = f"https://itunes.apple.com/search?term={query}&limit=5"
    r = requests.get(url)

    if r.status_code != 200:
        update.message.reply_text("❌ Error searching for songs.")
        return

    results = r.json().get("results", [])
    if not results:
        update.message.reply_text("No songs found.")
        return

    reply = "🎶 Search Results:\n"
    for track in results:
        reply += f"{track.get('trackName')} - {track.get('artistName')}\n"
        if track.get('previewUrl'):
            reply += f"{track.get('previewUrl')}\n\n"

    update.message.reply_text(reply)

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, search_song))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()