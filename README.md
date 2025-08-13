# Telegram Music Search Bot

## Features
- Search songs (worldwide + Myanmar) using iTunes API
- Returns song name, artist, and preview link
- Heroku-ready deployment

---

## Setup on Heroku
1. Create a new Heroku app
2. Go to **Settings → Config Vars**
3. Add:
   - `TELEGRAM_BOT_TOKEN` = your bot token from BotFather
4. Deploy code to Heroku (via GitHub or Heroku CLI)
5. Scale the worker:
   ```bash
   heroku ps:scale worker=1