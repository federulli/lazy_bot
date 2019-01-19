import os
from functools import wraps
import structlog

logger = structlog.get_logger()


def admin_only(func):
    @wraps(func)
    def restricted_func(bot, update, **kwargs):
        user = update.effective_user.username
        logger.msg('message received',
                   command=update.message.text,
                   username=user)
        if user == os.environ['ADMIN']:
            return func(bot, update, **kwargs)
        else:
            update.message.reply_text('🚫 No estás autorizado a usar este comando')
    return restricted_func
