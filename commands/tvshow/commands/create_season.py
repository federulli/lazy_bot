import requests
from ...utils import get_host
from decorators import admin_only
import structlog

from commands.tvshow.status import (
    READ_TV_SHOW_ID,
    CREATE_SEASON,
    END,
)
logger = structlog.get_logger()

from commands.queries import client, CREATE_SEASON_MUTATION


@admin_only
def add_season(bot, update):
    update.message.reply_text(
        'Ingrese el id de la serie:\n'
    )
    return READ_TV_SHOW_ID


def read_tv_show_id(bot, update, chat_data):
    chat_data['tv_show_id'] = update.message.text
    update.message.reply_text(
        'Ingrese la nueva temporada:\n'
    )
    return CREATE_SEASON


def create_season(bot, update, chat_data):
    message = 'OK'
    try:
        client.execute(
            CREATE_SEASON_MUTATION,
             {"show_id": chat_data['tv_show_id'], "number": update.message.text}
        )
    except Exception as e:
        logger.exception(str(e), exc_info=True)
        message = str(e)
    finally:
        bot.send_message(
            chat_id=update.message.chat_id,
            text=message
        )
    return END
