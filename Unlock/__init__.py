"""
This module initializes and starts two Pyrogram clients: one for the bot and one for a user bot.
It loads necessary configuration from environment variables, sets up logging, and starts both bots.
The bots interact with Telegram using their respective API credentials.

The bot uses:
- Bot Token from @BotFather
- API_ID and API_HASH from my.telegram.org
- A user session string for the user bot

Functions:
- rbot: The bot client to interact with the Telegram API using the provided Bot Token.
- ubot: The user client for accessing user-specific Telegram functionalities.
- Logs messages to track bot startup and operations.
"""

import os
import time
import logging

# Import necessary libraries
from dotenv import load_dotenv
from pyrogram import Client

# Load environment variables from .env file
load_dotenv()

# Set up logging to help debug and track the bot's activity
logging.basicConfig(
    level=logging.INFO,
    format=(
        '\033[32m%(asctime)s\033[0m | \033[36;1m%(levelname)s\033[0m | '
        '\033[31m%(module)s.%(funcName)s:\033[0m\033[35m%(lineno)d | \033[0m - '
        '\033[1m%(message)s\033[0m'
    ),
    datefmt='%H:%M:%S',
)

# Load sensitive information from the .env file
API_ID = os.getenv("API_ID")  # Telegram API ID
API_HASH = os.getenv("API_HASH")  # Telegram API Hash
BOT_TOKEN = os.getenv("BOT_TOKEN")  # Bot Token from BotFather
SESSION = os.getenv("SESSION_STRING")  # User session string (for user bot)
DEVELOPER = "@CoderX" # don't change.
MAX_ALLOWED_DOWNLOAD_SIZE = os.getenv("ALLOWED_DOWNLOAD_SIZE", 50)

# Check if all necessary environment variables are loaded
if not all([API_ID, API_HASH, BOT_TOKEN, SESSION]):
    logging.error("Missing one or more environment variables. Please check your .env file.")
    exit(1)

# Track bot startup time (useful for debugging uptime)
start_time = time.time()

# Initialize the bot for interacting with Telegram (Unlock bot)
rbot = Client(
    "Unlock",  # Bot's session name
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,  # Bot token provided by @BotFather
    plugins={"root": "Unlock.modules"}  # Path to your plugins folder for bot functionality
)

# Initialize the user bot for accessing user-specific Telegram functionalities
ubot = Client(
    "UserBot",  # User bot's session name
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION,  # User session string, can be generated using Pyrogram
    plugins={"root": "Unlock.modules.UserBot"}  # Path to your userbot's plugin directory
)
# Optional: Add functionality to track bot uptime or interactions with time.
# Use the `start_time` for future metrics if needed.
