import requests


def list_torrents(bot, update):
    r = requests.get('http://127.0.0.1:8080/query/torrents')
    bot.send_message(
        chat_id=update.message.chat_id,
        text='\n'.join("{} {:.2%} {}".format(
            torrent['name'],
            torrent['progress'],
            torrent['state']
        ) for torrent in r.json())
    )
