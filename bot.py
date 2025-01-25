import telebot

with open("token.txt", "r") as f:
    BOT_TOKEN = f.read()

bot = telebot.TeleBot(BOT_TOKEN)

import google.generativeai as genai

with open("gemini_token.txt", "r") as f:
    GEMINI_TOKEN = f.read()

genai.configure(api_key=GEMINI_TOKEN)
model = genai.GenerativeModel("gemini-1.5-flash")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    response = model.generate_content(message.text)
    bot.reply_to(message, response.text)

def main():
    bot.infinity_polling()

if __name__ == "__main__":
    main()