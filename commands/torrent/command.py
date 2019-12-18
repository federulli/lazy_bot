import requests
import structlog
from decorators import admin_only
from qbittorrent_api import get_torrents

logger = structlog.get_logger()


@admin_only
def list_torrents(bot, update):
    message = 'empty'
    try:
        torrents = get_torrents()
        if torrents:
            message = '\n\n'.join(
                "{}\n{:.2%}\n{}".format(
                    torrent['name'],
                    torrent['progress'],
                    torrent['state']
                ) for torrent in torrents
            )
    except Exception as e:
        message = str(e)
        logger.exception(str(e), exc_info=True)
    finally:
        bot.send_message(
            chat_id=update.message.chat_id,
            text=message
        )
