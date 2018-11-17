import requests
from ..utils import get_host


def list_torrents(bot, update):
    r = requests.get('{}/query/torrents'.format(get_host()))
    bot.send_message(
        chat_id=update.message.chat_id,
        text='\n'.join("{} {:.0f}% {}".format(
            torrent['name'],
            torrent['progress'],
            torrent['state']
        ) for torrent in r.json())
    )
