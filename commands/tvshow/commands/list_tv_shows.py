import requests
from ...utils import get_host
from decorators import admin_only
import structlog

logger = structlog.get_logger()


@admin_only
def list_tv_shows(bot, update):
    try:
        r = requests.get(
            '{}/tv-shows/'.format(get_host())
        )
        r.raise_for_status()
        bot.send_message(
            chat_id=update.message.chat_id,
            text='\n\n'.join(
                'id: {}\nname: {}'.format(
                    tv_show['id'],
                    tv_show['name']
                ) for tv_show in r.json()
            )
        )
    except:
        logger.exception("Error listing tv shows", exc_info=True)
