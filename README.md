WhatsApp AI AutoReply Bot
⚙️ Installation
1. Clone the repository
git clone https://github.com/Khatriprakhar1/WhatsApp-AI-AutoReply-Bot.git
cd WhatsApp-AI-AutoReply-Bot
2. Install dependencies
pip install pyautogui
pip install pyperclip
pip install openai

Or install all together:

pip install -r requirements.txt
🔑 Setup OpenAI API Key

Open the Python file and add your API key:

client = OpenAI(
  api_key="YOUR_API_KEY"
)

You can get your API key from:

https://platform.openai.com/api-keys