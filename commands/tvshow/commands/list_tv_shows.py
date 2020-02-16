import requests
from ...utils import get_host
from decorators import admin_only
import structlog

from commands.queries import client, GET_TV_SHOWS_QUERY

logger = structlog.get_logger()


@admin_only
def list_tv_shows(bot, update):
    try:
        response = client.execute(GET_TV_SHOWS_QUERY)
        logger.info(response)
        message = '\n\n'.join(
                'id: {}\nname: {}'.format(
                    tv_show['id'],
                    tv_show['name']
                ) for tv_show in response['tvShows']
        )
    except Exception as e:
        logger.exception(str(e), exc_info=True)
        message = str(e)
    finally:
        bot.send_message(
            chat_id=update.message.chat_id,
            text=message
        )
