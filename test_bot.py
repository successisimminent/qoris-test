#!/usr/bin/env python3
"""
Test script for the Telegram bot
"""

try:
    import bot
    print("✅ Bot import successful")
    print("✅ Bot token loaded:", bot.BOT_TOKEN[:10] + "..." if bot.BOT_TOKEN else "❌ No token")
except Exception as e:
    print("❌ Bot import failed:", str(e))