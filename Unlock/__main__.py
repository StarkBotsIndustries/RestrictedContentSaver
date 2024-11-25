"""
This file initializes and starts the bot and user bot clients using Pyrogram.
It ensures the bot operates in an asynchronous manner, handling errors gracefully
and logging all actions for transparency and debugging.

Copyright (c) 2024 StarkBotsIndustries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import logging
from pyrogram import idle

from . import rbot, ubot
from .modules.UserBot.Special.UniversalDatabase import initialize_database


async def main():
    """
    Starts the bot and user bot clients, waits for them to run, and shuts them down
    gracefully when the bot is stopped.
    """
    try:
        logging.info("Initializing Bot and UserBot...")

        # Start the bot and user bot clients
        await rbot.start()
        initialize_database()
        await ubot.start()
        logging.info("Bot and UserBot started successfully.")

    except Exception as error:
        # Log any exceptions that occur
        logging.exception("An error occurred: %s", error)
    
    else:
        # Idle to keep the bot running
        await idle()
        # Ensure graceful shutdown of the clients
        logging.info("Stopping Bot and UserBot...")
        try:
            await rbot.stop()
            await ubot.stop()
            logging.info("Bot and UserBot stopped successfully.")
        except Exception as shutdown_error:
            logging.error("Error during shutdown: %s", shutdown_error)

if __name__ == "__main__":
    # Run the main function with the bot
    try:
        rbot.run(main())
    except KeyboardInterrupt:
        logging.info("Keyboard interrupt received. Exiting...")
    except Exception as run_error:
        logging.error("Unexpected error: %s", run_error)
