import requests
from ...utils import get_host
from decorators import admin_only
import structlog

from commands.queries import client, CREATE_TV_SHOW_MUTATION

from commands.tvshow.status import (
    CREATE_TV_SHOW,
    END,
)
logger = structlog.get_logger()


@admin_only
def add_tv_show(bot, update):
    update.message.reply_text(
        'Ingrese el nombre de la serie:\n'
    )
    return CREATE_TV_SHOW


def create_tv_show(bot, update, chat_data):
    name = update.message.text
    try:
        response = client.execute(CREATE_TV_SHOW_MUTATION, {"name": name})
        logger.info(response)
        message = "{} id: {}".format(name, response['createTvShow']['tvShow']['id'])
    except Exception as e:
        logger.exception(str(e), exc_info=True)
        message = str(e)
    finally:
        bot.send_message(
            chat_id=update.message.chat_id,
            text=message
        )
    return END
