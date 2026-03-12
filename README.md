# Qoris Test

Test repository created by Qoris agent.

## Telegram Bot - Jarvis AI Assistant

This repository contains a Telegram bot built with Python and the aiogram library.

### Features

- Responds to `/start` command with a welcome message: "Hello! I am Jarvis, your AI assistant powered by Qoris."
- Handles all other text messages with: "I received your message. Jarvis is thinking..."
- Built with async Python using aiogram v3
- Uses uv for package management

### Setup

1. Install dependencies:
   ```bash
   uv add aiogram
   ```

2. Set the `TELEGRAM_BOT_TOKEN` environment variable with your bot token

3. Run the bot:
   ```bash
   uv run python bot.py
   ```

### Testing

Run the test script to validate the bot configuration:
```bash
uv run python test_bot.py
```

### Project Structure

- `bot.py` - Main bot application
- `test_bot.py` - Bot validation script
- `pyproject.toml` - uv project configuration with dependencies