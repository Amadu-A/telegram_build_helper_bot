# Dockerfile
FROM python:3.12-slim

# Установим рабочую директорию
WORKDIR /app

# Скопируем файлы проекта
COPY . .

# Установим зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем утилиту dos2unix для корректной работы с .env
RUN apt-get update && apt-get install -y --no-install-recommends dos2unix \
    && dos2unix /app/.env

# Устанавливаем python-dotenv для работы с переменными окружения
RUN pip install python-dotenv

# Команда запуска бота
CMD ["python", "-m", "bot.main"]
