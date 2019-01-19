from telegram.ext import (
    CommandHandler,
)

from commands.torrent.command import list_torrents

list_torrents_handler = CommandHandler(
    'list_torrents',
    list_torrents
)
