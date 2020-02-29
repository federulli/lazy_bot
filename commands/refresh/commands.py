from ..utils import get_host
import requests
import structlog

from commands.queries import client


logger = structlog.get_logger()


def refresh(bot, update, action):
    try:
        message = 'OK'
        client.execute(action)
    except Exception as e:
        message = str(e)
        logger.exception('ERROR refreshing',
                         exc_info=True)
    finally:
        bot.send_message(
            chat_id=update.message.chat_id,
            text=message
        )