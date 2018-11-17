import os
from functools import wraps


def admin_only(func):
    @wraps(func)
    def restricted_func(bot, update, **kwargs):
        user = update.effective_user.username
        if user == os.environ['ADMIN']:
            return func(bot, update, **kwargs)
        else:
            update.message.reply_text('🚫 No estás autorizado a usar este comando')
    return restricted_func
