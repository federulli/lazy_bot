import requests
from decorators import admin_only


@admin_only
def list_torrents(bot, update):
    r = requests.get('http://127.0.0.1:8080/query/torrents')
    bot.send_message(
        chat_id=update.message.chat_id,
        text='\n\n'.join("{}\n{:.2%}\n{}".format(
            torrent['name'],
            torrent['progress'],
            torrent['state']
        ) for torrent in r.json())
    )
