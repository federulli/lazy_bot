import requests
from ...utils import get_host
from decorators import admin_only
import structlog

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
    new_tv_show = {
        "name": name,
        "year": None
    }
    r = requests.post(
        '{}/tv-shows/'.format(get_host()),
        json=new_tv_show
    )
    bot.send_message(
        chat_id=update.message.chat_id,
        text="{} id: {}".format(name, r.json()['id'])
    )
    return END
