# telegram_build_helper_bot
telegram_build_helper_bot

```commandline
telegram_excel_bot/
├── bot/
│   ├── __init__.py         # Инициализация бота и импорт команд
│   ├── config.py           # Конфигурация бота (токен и настройки)
│   ├── handlers/
│   │   ├── __init__.py     # Инициализация обработчиков
│   │   ├── commands.py     # Обработчик команд
│   │   └── documents.py    # Обработчик загрузки документов
│   ├── utils/
│   │   ├── __init__.py     # Инициализация утилит
│   │   └── excel_compare.py# Функция для сравнения файлов Excel
│   └── main.py             # Главный файл для запуска бота
├── .env
├── Dockerfile
├── docker-compose.yml
├── README.md               # Описание проекта и инструкции
└── requirements.txt        # Зависимости проекта

```
# Telegram Excel Comparison Bot

Этот бот для Telegram принимает два Excel файла по команде `/compare`, сравнивает их содержимое и выдает результат.

## Описание
Бот использует `pytelegrambotapi` и `pandas` для работы с файлами и выполнением проверки на совпадение данных в таблицах.

## Установка и настройка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/telegram_excel_bot.git
   cd telegram_excel_bot
   pip install -r requirements.txt
   python bot/main.py
   ```
2. Создайте .env файл и укажите токен бота:
```commandline
BOT_TOKEN=your_telegram_bot_token
```
3. Запустите бота:
```commandline
python -m bot.main
```
Использование Docker
- Склонируйте репозиторий.

- Создайте .env файл с токеном бота, как описано выше.

- Постройте и запустите контейнеры:
```commandline
docker-compose up --build
```

Структура проекта

* bot/config.py - Конфигурация бота.
* bot/handlers/commands.py - Обработчик команд, таких как /start и /compare.
* bot/handlers/documents.py - Обработчик для загрузки и обработки файлов.
* bot/utils/excel_compare.py - Функция для сравнения данных в Excel.
* bot/main.py - Главный файл для запуска бота.

