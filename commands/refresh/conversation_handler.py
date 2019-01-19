from telegram.ext import CommandHandler

from commands.refresh.commands import (
    refresh
)


refresh_chapter_count_handler = CommandHandler(
    'refresh_chapter_count',
    lambda bot, update: refresh(bot, update, 'CHAPTER_COUNT')
)

delete_completed_handler = CommandHandler(
    'delete_completed',
    lambda bot, update: refresh(bot, update, 'DELETE_COMPLETED')
)

download_subtitles_handler = CommandHandler(
    'download_subtitles',
    lambda bot, update: refresh(bot, update, 'SUBTITLES')
)

download_not_found_movies_handler = CommandHandler(
    'download_not_found_movies',
    lambda bot, update: refresh(bot, update, 'MOVIE')
)

download_not_found_chapters_handler = CommandHandler(
    'download_not_found_chapters',
    lambda bot, update: refresh(bot, update, 'TVSHOW')
)
