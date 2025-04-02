from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Токен вашего бота
BOT_TOKEN = '7517508116:AAHydfYGo0-6pYS3rwx0GE2__ELVhi9pwnE'

# Функция для обработки команды /start
def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    # Отправка сообщения с кнопкой, которая открывает WebApp
    keyboard = [[InlineKeyboardButton("Запустить WebApp", url="https://awdawd-gray.vercel.app/")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text(
        f"Привет, {user.first_name}!\nНажмите на кнопку ниже, чтобы открыть Mini App.",
        reply_markup=reply_markup
    )

# Основная функция для запуска бота
def main():
    updater = Updater(BOT_TOKEN)

    # Регистрация обработчиков
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
