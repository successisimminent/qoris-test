#!/usr/bin/env python3
"""
Telegram Bot - Jarvis AI Assistant
Powered by Qoris Runtime using Groq API
"""

import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from openai import OpenAI

# Configure logging to both console and file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Get tokens from environment variables
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

if not BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN environment variable is not set")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set")

# Initialize Groq client
groq_client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    Handle /start command
    """
    try:
        logger.info(f"User {message.from_user.id} started the bot")
        await message.answer("Hello! I am Jarvis, your AI assistant powered by Qoris and Groq.")
    except Exception as e:
        logger.error(f"Error in start handler: {str(e)}", exc_info=True)
        await message.answer("Sorry, I encountered an error. Please try again.")


async def generate_response(user_message: str) -> str:
    """
    Generate AI response using Groq API
    """
    try:
        logger.info(f"Generating response for message: {user_message[:100]}...")
        
        response = groq_client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "system", "content": "You are Jarvis, a helpful AI assistant. Be concise and helpful."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        ai_response = response.choices[0].message.content
        logger.info(f"Generated response: {ai_response[:100]}...")
        return ai_response
        
    except Exception as e:
        logger.error(f"Error generating AI response: {str(e)}", exc_info=True)
        return "I apologize, but I'm having trouble processing your request right now. Please try again later."


@dp.message()
async def message_handler(message: types.Message) -> None:
    """
    Handle all other text messages with AI responses
    """
    try:
        user_id = message.from_user.id
        user_message = message.text
        
        logger.info(f"Received message from user {user_id}: {user_message}")
        
        # Send typing action
        await bot.send_chat_action(chat_id=message.chat.id, action="typing")
        
        # Generate AI response
        ai_response = await generate_response(user_message)
        
        # Send the response
        await message.answer(ai_response)
        
        logger.info(f"Sent response to user {user_id}")
        
    except Exception as e:
        logger.error(f"Error in message handler: {str(e)}", exc_info=True)
        try:
            await message.answer("Sorry, I encountered an error processing your message. Please try again.")
        except Exception as send_error:
            logger.error(f"Failed to send error message: {str(send_error)}", exc_info=True)


async def main() -> None:
    """
    Main function to start the bot
    """
    logger.info("Starting Jarvis Telegram Bot with Groq API...")
    logger.info("Bot is ready to receive messages!")
    
    try:
        # Start polling
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Error in main polling loop: {str(e)}", exc_info=True)


if __name__ == "__main__":
    asyncio.run(main())