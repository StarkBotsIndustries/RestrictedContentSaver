"""
Media Saver Module

This script handles downloading media files from Telegram messages, caching them, and
re-uploading them to a specified channel for easier access and sharing.

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
    - UniversalDatabase (for data caching and retrieval)
    - UserBot instance (`ubot`)
"""

import os
import logging

from pyrogram.types import Message
from pyrogram.enums import MessageMediaType

from ... import ubot, MAX_ALLOWED_DOWNLOAD_SIZE
from .Special.UniversalDatabase import SD, channel_id, INVITE_LINK




def bytes_to_mb(bytes: int) -> float:
    """
    Convert bytes to megabytes (MB).

    Args:
        bytes (int): The size in bytes.

    Returns:
        float: The size in MB.
    """
    return bytes / 1048576


async def saver(m: Message, chat_id: int, msg_id: int, chat_type: str, joining_link: str = None, processing_msg = None) -> dict:
    """
    Save media from a Telegram message, process it, and optionally cache it.

    Args:
        m (Message): Incoming message object from Pyrogram.
        chat_id (int): The ID of the chat containing the target message.
        msg_id (int): The ID of the message containing media.
        chat_type (str): Type of chat - "private" or "public".
        joining_link (str, optional): Link to join a private chat, if required.

    Returns:
        dict: Details about the saved media, or an error message.
    """
    # Attempt to join the private chat if required
    if chat_type == "private":
        try:
            await ubot.join_chat(joining_link)
        except Exception as e:
            logging.error("Failed to join chat: %s", e)
            return "Can't join the chat"

    try:
        await ubot.join_chat(INVITE_LINK)
    except:
        pass
    # Fetch the specified message
    try:
        msg = await ubot.get_messages(chat_id, int(msg_id))
    except Exception as e:
        logging.error("Failed to fetch message: %s", e)
        await processing_msg.edit_text(f"Error: {e}")
        return None

    if msg.empty is True:
        await processing_msg.edit_text("Are you sure?")
        return None
    # Check if the media is already cached
    cached = SD().read_data(msg.link)
    if cached:
        return {
            "ChannelMessageID": cached["message_id"],
            "ChannelUsername": channel_id,
            "IsCached": True,
        }

    # Determine media type and file size
    file_id, file_type, size = None, None, 0
    if msg.media:
        media_map = {
            MessageMediaType.PHOTO: ("photo", lambda x: x.photo.file_size),
            MessageMediaType.VIDEO: ("video", lambda x: x.video.file_size),
            MessageMediaType.AUDIO: ("audio", lambda x: x.audio.file_size),
            MessageMediaType.VOICE: ("voice", lambda x: x.voice.file_size),
            MessageMediaType.DOCUMENT: ("document", lambda x: x.document.file_size),
            MessageMediaType.VIDEO_NOTE: ("video_note", lambda x: x.video_note.file_size),
            MessageMediaType.STORY: ("story", lambda x: x.story.file_size),
        }

        file_type, size_func = media_map.get(msg.media, (None, None))
        if file_type:
            file_id = getattr(msg, file_type).file_id
            size = size_func(msg)

    # Validate file size
    if bytes_to_mb(size) > MAX_ALLOWED_DOWNLOAD_SIZE:
        await processing_msg.edit_text("File is too large. The limit is 50MB, you can subscribe to premium for limits upto 4GB. To upgrade pm: @CoderX")
        return None

    if msg.chat.has_protected_content == False:
        await processing_msg.edit_text("Bruh, the channel isn't even restricted...")
        return None
    # Retrieve caption or fallback to text
    caption = msg.caption or msg.text or None

    # Download and upload the media to the caching channel
    datasave, file_path = False, None
    down_thumb = None
    if file_type:
        try:
            if file_type == "audio":
                file_path = await ubot.download_media(file_id)
                try:
                    down_thumb = await ubot.download_media(msg.audio.thumbs[0])
                except:
                    down_thumb = "Unlock/stark_thumb.jpg"
                msgg = await ubot.send_audio(chat_id=channel_id, audio=file_path, caption=caption, performer=msg.audio.performer, title=msg.audio.title, file_name=msg.audio.file_name, duration=msg.audio.duration, thumb=down_thumb)
                cache_msg_id = msgg.id
                datasave = True
            elif file_type == "document":
                file_path = await ubot.download_media(file_id)
                msgg = await ubot.send_document(chat_id=channel_id, document=file_path, file_name=msg.document.file_name, thumb="Unlock/stark_thumb.jpg", caption=msg.caption)
                cache_msg_id = msgg.id
                datasave = True
            elif file_type == "video":
                file_path = await ubot.download_media(file_id)
                msgg = await ubot.send_video(chat_id=channel_id, video=file_path, duration=msg.video.duration, width=msg.video.width, height=msg.video.height, thumb="Unlock/stark_thumb.jpg", file_name=msg.video.file_name, supports_streaming=msg.video.supports_streaming, ttl_seconds=msg.video.ttl_seconds, caption=msg.caption)
                cache_msg_id = msgg.id
                datasave = True
            elif file_type == "photo":
                file_path = await ubot.download_media(file_id)
                msgg = await ubot.send_photo(chat_id=channel_id, photo=file_path,has_spoiler=1, caption=msg.caption)
                cache_msg_id = msgg.id
                datasave = True
            elif file_type == "voice":
                file_path = await ubot.download_media(file_id)
                msgg = await ubot.send_voice(chat_id=channel_id, voice=file_path, duration=msg.voice.duration)
                cache_msg_id = msgg.id
                datasave = True
            else:
                file_path = await ubot.download_media(file_id)
                upload_func = getattr(ubot, f"send_{file_type}")
                msgg = await upload_func(channel_id, file_path, caption=caption)
                cache_msg_id = msgg.id
                datasave = True
        except Exception as e:
            logging.error(f"Error handling {file_type}: {e}")
            return "ERROR WITH USERBOT"

    try:
        os.remove(file_path)
        os.remove(down_thumb)
    except:
        pass
    # Cache the file information if successfully saved
    if datasave:
        SD().write_data(cache_msg_id, msg.link, m.from_user.id, file_type)
        return {
            "IsCached": False,
            "Thumb": down_thumb or "Unlock/stark_thumb.jpg",
            "MsgID": msgg.id
        }

    # If media is unsupported
    await m.reply_text(msg.text)
    return None
