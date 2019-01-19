import os
import structlog

from telegram.ext import (
    Updater,
    CommandHandler,
)

from commands.tvshow.conversation_handler import (
    tv_show_conversation_handler,
    season_conversation_handler,
    list_seasons_conversation_handler,
    list_tv_shows_handler,
)

from commands.movie.conversation_handler import (
    movie_conversation_handler,
    list_movies_handler
)

from commands.torrent.conversation_handler import list_torrents_handler

from commands.refresh.conversation_handler import (
    refresh_chapter_count_handler,
    delete_completed_handler,
    download_not_found_chapters_handler,
    download_subtitles_handler,
    download_not_found_movies_handler,
)
structlog.configure()
logger = structlog.get_logger()


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


updater = Updater(token=os.environ['TOKEN'])

dispatcher = updater.dispatcher


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# TV SHOW
dispatcher.add_handler(tv_show_conversation_handler)

dispatcher.add_handler(list_tv_shows_handler)

# TORRENT #

dispatcher.add_handler(list_torrents_handler)

# MOVIES #

dispatcher.add_handler(list_movies_handler)

dispatcher.add_handler(movie_conversation_handler)

# SEASONS #

dispatcher.add_handler(season_conversation_handler)

dispatcher.add_handler(list_seasons_conversation_handler)

dispatcher.add_handler(refresh_chapter_count_handler)
dispatcher.add_handler(delete_completed_handler)
dispatcher.add_handler(download_not_found_chapters_handler)
dispatcher.add_handler(download_subtitles_handler)
dispatcher.add_handler(download_not_found_movies_handler)

try:
    logger.msg("Starting Lazy Bot")
    updater.start_polling()
except Exception as e:
    logger.exception("ERROR", exc_info=True)
