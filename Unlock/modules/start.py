"""
This bot saves restricted content and makes it accessible to users via commands. 
Includes commands for start, help, and ToS.

Author:
    - @CoderX on Telegram
    - @Snehashish06 on GitHub

Project:
    - Developed for the @StarkBots channel on Telegram.

License:
    This code is open-source and can be reused or modified under the following conditions:
    1. Proper credits must be given to the original authors.
    2. A link to the original source must be included in derivative works.

Disclaimer:
    This project was coded solely for learning purposes. The owner will not be held responsible
    for any misuse, illegal activities, or violations of Terms of Service (ToS) of any platform 
    arising from the use or modification of this code. Users are strongly advised to comply with 
    the applicable rules and regulations of the services they interact with.

Dependencies:
    - Pyrogram
"""

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


@Client.on_message(filters.command("start"))
async def start(bot: Client, m: Message):
    """
    Handle the /start command. Sends a welcoming message to the user with buttons for navigation.

    Args:
        bot (Client): The bot client instance.
        m (Message): Incoming message object.
    """
    photo = "https://imgur.com/a/oukNSXa"  # Replace with a valid image URL
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🌟 Updates Channel 🌟", url="https://t.me/StarkBots"),
                InlineKeyboardButton("🍀 Support Chat 🍀", url="https://t.me/StarkBotsChat")
            ],
            [
                InlineKeyboardButton("🧑‍💻 Developer 🧑‍💻", callback_data="developer"),
                InlineKeyboardButton("📜 ToS 📜", callback_data="tos")
            ]
        ]
    )
    start_text = (
        "🌟 **Welcome to Restricted Content Saver Bot!** 🌟\n\n"
        "✨ **Features:**\n"
        "🔹 Save restricted content easily.\n"
        "🔹 Retrieve content with simple commands.\n"
        "🔹 Open-source for transparency.\n\n"
        "📝 **Usage:**\n"
        "1️⃣ Send the link of restricted content to save.\n"
        "2️⃣ Use commands like `/save` to retrieve content.\n\n"
        "For help, click on **Help** or type `/help`."
    )
    await m.reply_photo(photo=photo, caption=start_text, reply_markup=btn)


@Client.on_message(filters.command("help"))
async def help(bot: Client, m: Message):
    """
    Handle the /help command. Provides details about bot features and usage.

    Args:
        bot (Client): The bot client instance.
        m (Message): Incoming message object.
    """
    help_text = (
        "**🆘 Help - Restricted Content Saver Bot**\n\n"
        "🔹 **Commands:**\n"
        "• `/start`: Start the bot and view the welcome message.\n"
        "• `/help`: Display this help message.\n"
        "• `/repo`: View the bot's source code.\n"
        "• `/tos`: Read the bot's terms of service.\n\n"
        "🔹 **How to Use:**\n"
        "1️⃣ Send a restricted content link to the bot.\n"
        "2️⃣ The bot will save the content for you.\n\n"
        "For further assistance, join our **Support Chat**."
    )
    await m.reply_text(help_text)


@Client.on_message(filters.command("tos"))
async def tos(bot: Client, m: Message):
    """
    Handle the /tos command. Displays the bot's Terms of Service.

    Args:
        bot (Client): The bot client instance.
        m (Message): Incoming message object.
    """
    tos_text = (
        "**📜 Terms of Service - Restricted Content Saver Bot**\n\n"
        "1️⃣ This bot is for educational purposes only.\n"
        "2️⃣ The owner is not responsible for any misuse or violation of platform ToS.\n"
        "3️⃣ Users must comply with all applicable laws and platform policies.\n"
        "4️⃣ The bot reserves the right to ban users for abuse or misuse.\n\n"
        "By using this bot, you agree to these terms."
    )
    await m.reply_text(tos_text)



@Client.on_callback_query(filters.regex("tos"))
async def tos_callback(bot: Client, q: CallbackQuery):
    """
    Handle ToS button callback. Displays the bot's Terms of Service.

    Args:
        bot (Client): The bot client instance.
        q (CallbackQuery): Incoming callback query object.
    """
    btn = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Back 🔙", callback_data="back")]
        ]
    )
    tos_text = (
        "**📜 Terms of Service - Restricted Content Saver Bot**\n\n"
        "1️⃣ This bot is for educational purposes only.\n"
        "2️⃣ The owner is not responsible for any misuse or violation of platform ToS.\n"
        "3️⃣ Users must comply with all applicable laws and platform policies.\n"
        "4️⃣ The bot reserves the right to ban users for abuse or misuse.\n\n"
        "By using this bot, you agree to these terms."
    )
    await q.message.edit_text(tos_text, reply_markup=btn)


@Client.on_callback_query(filters.regex("back"))
async def back_to_home(bot: Client, q: CallbackQuery):
    """
    Handle back button callback. Returns to the start message.

    Args:
        bot (Client): The bot client instance.
        q (CallbackQuery): Incoming callback query object.
    """
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🌟 Updates Channel 🌟", url="https://t.me/StarkBots"),
                InlineKeyboardButton("🍀 Support Chat 🍀", url="https://t.me/StarkBotsChat")
            ],
            [
                InlineKeyboardButton("🧑‍💻 Developer 🧑‍💻", callback_data="developer"),
                InlineKeyboardButton("📜 ToS 📜", callback_data="tos")
            ]
        ]
    )
    back_text = (
        "🌟 **Welcome back to Restricted Content Saver Bot!** 🌟\n\n"
        "✨ **Features:**\n"
        "🔹 Save restricted content easily.\n"
        "🔹 Retrieve content with simple commands.\n\n"
        "For help, click on **Help** or type `/help`."
    )
    await q.edit_message_text(back_text, reply_markup=btn)