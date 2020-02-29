import requests
from ...utils import get_host
from decorators import admin_only
import structlog

from commands.tvshow.status import (
    END,
    LIST_SEASONS,
)

from commands.queries import client, LIST_SEASONS_QUERY


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
        response = client.execute(LIST_SEASONS_QUERY, {'tv_show_id': tv_show_id})
        message = "\n\n".join(
                'id: {}\nnumber: {}\ncompleted: {}\nepisode_count: {}\nepisodes: {}'.format(
                    season['id'],
                    season['number'],
                    season['completed'],
                    season['chapterCount'],
                    [chapter['number'] for chapter in season['chapters']]
                )
                for season in response['seasons']
            )
    except Exception as e:
        logger.exception('ERROR', exc_info=True)
        message = str(e)
    finally:
        bot.send_message(
            chat_id=update.message.chat_id,
            text=message
        )
    return END
