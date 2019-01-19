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
    r = requests.post(
        "{}/tv-shows/{}/seasons/".format(
            get_host(),
            chat_data['tv_show_id']
        ),
        json={"number": update.message.text}
    )
    bot.send_message(
        chat_id=update.message.chat_id,
        text=r.status_code
    )
    return END
