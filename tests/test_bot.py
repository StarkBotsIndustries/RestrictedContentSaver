# pip install pytest pytest-asyncio

import pytest
import logging
from pyrogram import Client
from pyrogram.errors import FloodWait
from unittest.mock import patch

# Test to check bot starts and stops correctly

@pytest.mark.asyncio
async def test_bot_start_stop():
    bot = Client("Unlock")  # Use your actual Client configuration here

    # Test bot start
    with patch.object(bot, 'start', return_value=None):  # Mocking start method
        await bot.start()  # Should run without errors

    # Test bot stop
    with patch.object(bot, 'stop', return_value=None):  # Mocking stop method
        await bot.stop()  # Should run without errors

    assert bot.is_alive() is False  # Check bot is stopped

# Test for invalid token (simulate error handling)
@pytest.mark.asyncio
async def test_bot_invalid_token():
    invalid_bot = Client("Unlock", bot_token="invalid_token")

    # Simulating an invalid token error
    with pytest.raises(FloodWait):
        await invalid_bot.start()

