from bot.handlers import commands, documents
from bot.config import BOT_TOKEN, bot
from telebot import TeleBot



if __name__ == "__main__":
    bot.polling(none_stop=True)
