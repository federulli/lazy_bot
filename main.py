import os
from telegram.ext import (
    Updater,
    CommandHandler,
)

from commands.tvshow.conversation_handler import(
    tv_show_conversation_handler,
    season_conversation_handler,
)

from commands.tvshow.commands import (
    list_tv_shows,
)

from commands.torrent.command import list_torrents


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


updater = Updater(token=os.environ['TOKEN'])

dispatcher = updater.dispatcher


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


dispatcher.add_handler(tv_show_conversation_handler)
dispatcher.add_handler(season_conversation_handler)

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
