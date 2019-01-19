from telegram.ext import ConversationHandler


def get_host():
    return "http://127.0.0.1:8000"


def cancel(bot, update):
    update.effective_message.reply_text('Operación cancelada')
    return ConversationHandler.END
