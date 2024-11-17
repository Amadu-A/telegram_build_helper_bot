import os
from dotenv import load_dotenv
from telebot import TeleBot

load_dotenv()  # Загружает переменные из .env файла
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = TeleBot(BOT_TOKEN)

print("Значение BOT_TOKEN:", BOT_TOKEN)  # Проверьте, выводится ли токен
