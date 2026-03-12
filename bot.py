#!/usr/bin/env python3
"""
Telegram Bot - Jarvis AI Assistant
Powered by Qoris Runtime
"""

import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get bot token from environment variable
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

if not BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN environment variable is not set")

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    Handle /start command
    """
    await message.answer("Hello! I am Jarvis, your AI assistant powered by Qoris.")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handle all other text messages
    """
    await message.answer("I received your message. Jarvis is thinking...")


async def main() -> None:
    """
    Main function to start the bot
    """
    logger.info("Starting Jarvis Telegram Bot...")
    logger.info("Bot is ready to receive messages!")
    
    # Start polling
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())