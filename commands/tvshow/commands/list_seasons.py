import requests
from ...utils import get_host
from decorators import admin_only
import structlog

from commands.tvshow.status import (
    END,
    LIST_SEASONS,
)
logger = structlog.get_logger()


@admin_only
def list_seasons(bot, update):
    update.message.reply_text(
        'Ingrese el id de la serie:\n'
    )
    return LIST_SEASONS


def get_seasons(bot, update, chat_data):
    try:
        tv_show_id = int(update.message.text)
        r = requests.get(
            '{}/tv-shows/{}/seasons/'.format(get_host(), tv_show_id),
        )
        r.raise_for_status()
        bot.send_message(
            chat_id=update.message.chat_id,
            text="\n\n".join(
                'id: {}\nnumber: {}\ncompleted: {}\nchapter_count: {}\nchapters: {}'.format(
                    season['id'],
                    season['number'],
                    season['completed'],
                    season.get('chapter_count', 0),
                    season.get('chapters', [])
                )
                for season in r.json()
            )
        )
    except Exception:
        logger.exception('ERROR', exc_info=True)
    return END
