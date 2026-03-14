WhatsApp AI AutoReply Bot

A simple Python bot that reads messages from WhatsApp Web and automatically generates replies using the OpenAI API.

Features

Reads chat messages automatically

Detects the latest message in the chat

Generates AI responses

Sends replies automatically

Supports Hindi + English style responses

Requirements

Python 3.x

WhatsApp Web opened in browser

Install dependencies:

pip install pyautogui pyperclip openai
Setup

Add your OpenAI API key in the script:

client = OpenAI(api_key="YOUR_API_KEY")
Run

Open WhatsApp Web

Open the chat you want the bot to reply in

Run:

python bot.py

The bot will read the chat, generate a response, and send it automatically.

Note

Mouse coordinates used in pyautogui may need adjustment depending on your screen resolution.