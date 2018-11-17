from telegram.ext import (
    Updater,
    CommandHandler,
    Filters,
    MessageHandler,
)

from commands.tvshow.commands import (
    add_tv_show,
    add_season,
    list_tv_shows,
)
from commands.torrent.command import list_torrents


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


updater = Updater(token='789083442:AAGIPWdm1-VJ1aGSJR4-0x6FYH0sU-bgt6o')

dispatcher = updater.dispatcher


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

add_tv_show_handler = CommandHandler(
    'add_tv_show',
    add_tv_show,
    pass_args=True
)
dispatcher.add_handler(add_tv_show_handler)

add_season_handler = CommandHandler(
    'add_season',
    add_season,
    pass_args=True
)
dispatcher.add_handler(add_season_handler)

list_tv_shows_handler = CommandHandler(
    'list_tv_shows',
    list_tv_shows
)
dispatcher.add_handler(list_tv_shows_handler)

list_torrents_handler = CommandHandler(
    'list_torrents',
    list_torrents
)
dispatcher.add_handler(list_torrents_handler)


updater.start_polling()
