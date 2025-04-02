from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BOT_TOKEN = '7517508116:AAHydfYGo0-6pYS3rwx0GE2__ELVhi9pwnE'
CHAT_ID = '7477642275'
API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'

# Функция для отправки данных в Telegram
def send_to_telegram(message):
    data = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.post(API_URL, data=data)
    return response

@app.route('/')
def index():
    return 'Server is running'

@app.route('/send_data', methods=['POST'])
def send_data():
    user_data = request.json  # Получаем данные от клиента в формате JSON
    message = f"Данные от пользователя:\n{user_data}"

    # Отправляем данные в Telegram
    send_to_telegram(message)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
