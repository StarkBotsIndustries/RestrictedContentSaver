"""
Interact with the bot to save and retrieve files using provided Telegram message links.

This script uses the Pyrogram library to process private and public message links,
retrieve the associated files via a UserBot, and send them to the requesting user.

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
    This project was coded solely for learning purposes. The owner will not be responsible
    for any illegal use, misuse, or violation of Terms of Service (ToS) of any platform.
    Users are advised to adhere to the rules and regulations of the platforms they interact with.

Functions:
    - identify_message_type(url): Determines if a given URL is for a private or public chat.
    - save_file(bot, m): Main handler for the `/save` command, retrieves and sends the file.

Dependencies:
    - Pyrogram
    - UserBot (for saver functionality)
"""

import re
import os

from pyrogram import Client, filters
from pyrogram.types import Message

from .UserBot.Special.UniversalDatabase import channel_id
from .UserBot.saver import saver, ubot  # Ensure this module is properly documented and available.

def identify_message_type(url: str) -> str:
    """
    Identify the type of chat based on the provided Telegram URL.

    Args:
        url (str): The Telegram message URL.

    Returns:
        str: "public" if the URL corresponds to a public chat,
             "private" if it corresponds to a private chat,
             None if the URL format is invalid.
    """
    private_chat_pattern = r"https://t\.me/c/\d+/\d+"
    public_chat_pattern = r"https://t\.me/[\w\d_]+/\d+"

    if re.fullmatch(public_chat_pattern, url):
        return "public"
    elif re.fullmatch(private_chat_pattern, url):
        return "private"
    else:
        return None

@Client.on_message(filters.command("save") & filters.private)
async def save_file(bot: Client, m: Message):
    """
    Handle the `/save` command to save and send files to the user.

    Args:
        bot (Client): The Pyrogram bot instance.
        m (Message): The incoming message containing the `/save` command.
    """
    text = m.text[len("/save "):].strip()  # Extract the URL from the command
    chat_type = identify_message_type(text)

    if chat_type is None:
        return await m.reply_text("Invalid message link. Format: https://t.me/chat/123")

    msg_id = text.split("/")[-1]  # Extract message ID from the URL
    if chat_type == "private":
        chat_id = int(f"-100{text.split('/')[-2]}")  # Extract private chat ID
    else:
        chat_id = text.split("/")[-2]  # Extract public chat ID

    joining_link = None
    if chat_type == "private":
        ask_msg = await m.chat.ask("Please send the joining link of the private chat:")
        joining_link = ask_msg.text  # Joining link for private chats

    processing_msg = await m.reply_text("Processing... Please wait. It might take a minute or two depending on the file size.")
    save_result = await saver(m, chat_id, msg_id, chat_type, joining_link, processing_msg)

    # Handle potential errors
    if save_result == "Can't join the chat":
        await m.reply_text("Unable to join the private chat. Please verify the joining link.")
        return await processing_msg.delete()
    elif save_result == "ERROR WITH USERBOT":
        await m.reply_text("An error occurred while saving the file. Please try again.")
        return await processing_msg.delete()
    elif save_result == None:
        return

    # Handle successful save
    if save_result["IsCached"]:
        channel_username = save_result["ChannelUsername"]
        message_id = save_result["ChannelMessageID"]
        await processing_msg.delete()
        await bot.copy_message(chat_id=m.chat.id, from_chat_id=channel_username, message_id=message_id)
        # await bot.send_message(
        #     chat_id=m.chat.id,
        #     text="**Note:** If the file extension is incorrect, you can rename the file to the correct extension."
        # # )
    else:
        await processing_msg.delete()
        await bot.copy_message(chat_id=m.chat.id, from_chat_id=channel_id, message_id=save_result["MsgID"])

    # Leave the private chat if applicable
    if chat_type == "private":
        await ubot.leave_chat(chat_id)
