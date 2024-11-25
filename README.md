# Restricted Content Saver Bot

> A **Telegram Bot** designed to save and retrieve restricted content seamlessly. This bot allows users to access restricted media by using simple commands. Built with Python and Pyrogram, it is a beginner-friendly project that you can easily clone, run, and customize.

---

## Features

- Save and retrieve restricted media such as photos, videos, and documents.
- Support for inline buttons and rich user interactions.
- Clear terms of service and help features.
- User-friendly interface with callback navigation.

---

## Getting Started

Follow these steps to clone and run the bot on your local machine.

### Prerequisites

1. **Python 3.9+** installed on your system.
2. **Telegram API Credentials**:
   - **Bot Token**: Obtain from [BotFather](https://t.me/BotFather).
   - **API_ID** and **API_HASH**: Get them from [my.telegram.org](https://my.telegram.org).
   - **SESSION**: You can use https://github.com/ShivangKakkar/StringSessionBot

---

### Installation Steps (Python 3.11 or below)

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/YourGitHubUsername/RestrictedContentSaver.git
   cd RestrictedContentSaver
   ```

2. **Install Dependencies**  
   Install the required Python packages using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**  
   Rename the example `.env.example` file to `.env`:
   ```bash
   mv .env.example .env
   ```
   Then, edit the `.env` file to add your `TOKEN`, `API_ID`, and `API_HASH`:
   ```
   TOKEN=your_bot_token_here
   API_ID=your_api_id_here
   API_HASH=your_api_hash_here
   SESSION=your_string_session_here
   MAX_ALLOWED_DOWNLOAD_SIZE = 50 # in Megabytes
   ```

4. **Run the Bot**  
   Use the following command to start the bot:
   ```bash
   python -m Unlock
   ```

> Your userbot must be an admin in our universal cache channel else bot won't work, ping us in support chat to get it in.

---

## Usage

### Commands

- **/start**: Start the bot and display a welcome message.
- **/help**: View bot features and usage instructions.
- **/repo**: Get the link to the bot's source code.
- **/tos**: Read the bot's Terms of Service.
- **/save** <link>: Get the restricted content.. 

### Features

- Send restricted media links to the bot to save and retrieve content.
- Inline buttons for quick navigation:
  - Updates Channel
  - Support Chat
  - Developer Information
- Logs are automatically generated for error tracking.

---

## Known Issues

This project is in its **initial stages** and might have bugs or incomplete features. If you encounter any issues, please report them in the [Support Chat](https://t.me/StarkBotsChat). Logs will help us debug the problem faster, so be sure to include them when reporting.

---

## Logs

Logs are automatically created during bot runtime to help track errors and user actions. Make sure to check your terminal or console for detailed logs.

---

## Contributing

We welcome contributions! Please check [contribution guidelines](https://github.com/StarkBotsIndustries/RestrictedContentSaver/CONTRIBUTING.MD).

---

### Authors
This project is maintained and developed by **StarkBotsIndustries** and its contributors. We appreciate your interest and contributions to this open-source project. For any queries or discussions, feel free to join our [support chat](https://t.me/StarkBotsChat) or follow updates on our [channel](https://t.me/StarkBots).

---
### LICENSE
- This project is distributed under the [MIT License](LICENSE).
---
### Conditions of Use

- A copy of the original license and copyright notice must be included in all significant portions of the software.
- If you distribute or modify this software, please ensure that you retain the original license and include a link to the [original source code repository](https://github.com/StarkBotsIndustries/RestrictedContentSaver).

**Disclaimer**:  
The software is provided "AS IS," without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. The authors or copyright holders will not be held liable for any claims, damages, or other liabilities arising from the software's use or misuse.

---

## Contact

- **Support Chat**: [@StarkBotsChat](https://t.me/StarkBotsChat)
- **Updates Channel**: [@StarkBots](https://t.me/StarkBots)