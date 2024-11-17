from telebot import types
from bot.config import BOT_TOKEN, bot
from bot.handlers.documents import file_data
# from telebot import TeleBot


# bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message: types.Message):
    bot.send_message(message.chat.id, "Привет! Отправь команду /compare и два Excel-файла для сравнения.")

@bot.message_handler(commands=['compare'])
def compare_files(message: types.Message):
    chat_id = message.chat.id
    file_data[chat_id] = []  # Инициализируем список для хранения файлов
    bot.send_message(chat_id, "Отправьте два Excel-файла.")
