from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# تم إضافة التوكن الخاص بالبوت
TOKEN = '7868065833:AAHTObI0OQhV7amLE-hzjgLkX05g41PPapQ'

# الدالة لعرض الزر
def start(update, context):
    keyboard = [
        [InlineKeyboardButton("اضغط هنا", callback_data='button_click')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('مرحباً! البوت قيد التصميم.', reply_markup=reply_markup)

# الدالة لمعالجة الضغط على الزر
def button(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="البوت قيد التصميم. شكراً لتفاعلك!")

# إنشاء البوت وتشغيله
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
