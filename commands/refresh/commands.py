from ..utils import get_host
import requests
import structlog

logger = structlog.get_logger()


def refresh(bot, update, type):
    try:
        r = requests.post(
            "{}/refresh/".format(get_host()),
            json={"type": type}
        )
        r.raise_for_status()
        bot.send_message(
            chat_id=update.message.chat_id,
            text='OK {}'.format(type)
        )
    except Exception:
        logger.exception('ERROR refreshing',
                         type=type,
                         exc_info=True)
