from telebot import types
from io import BytesIO
from bot.utils.excel_compare import compare_excel_files
from bot.config import BOT_TOKEN, bot
# from telebot import TeleBot

# bot = TeleBot(BOT_TOKEN)

# Словарь для хранения файлов по chat_id
file_data = {}

@bot.message_handler(content_types=['document'])
def handle_docs(message: types.Message):
    chat_id = message.chat.id

    # Проверяем, ожидает ли бот два файла для данного chat_id
    if chat_id in file_data and len(file_data[chat_id]) < 2:
        # Загружаем файл
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        file_data[chat_id].append(BytesIO(downloaded_file))

        # Если два файла получены, запускаем сравнение
        if len(file_data[chat_id]) == 2:
            bot.send_message(chat_id, "Файлы получены. Начинаю сравнение...")
            result = compare_excel_files(file_data[chat_id][0], file_data[chat_id][1])
            bot.send_message(chat_id, result)
            file_data.pop(chat_id)  # Удаляем данные файлов после сравнения
        else:
            bot.send_message(chat_id, "Ожидаю второй файл для сравнения.")
    else:
        bot.send_message(chat_id, "Сначала отправьте команду /compare.")
