from telegram.ext import CommandHandler

from commands.refresh.commands import (
    refresh
)

from commands.queries import (
    SEARCH_MOVIES_MUTATION,
    SEARCH_EPISODES_MUTATION,
    DELETE_COMPLETED_TORRENTS_MUTATION,
    RELOAD_CHAPTER_COUNT_MUTATION,
    DELETE_ALL_TORRENTS_MUTATION,
) 

refresh_chapter_count_handler = CommandHandler(
    'refresh_chapter_count',
    lambda bot, update: refresh(bot, update, RELOAD_CHAPTER_COUNT_MUTATION)
)

delete_completed_handler = CommandHandler(
    'delete_completed',
    lambda bot, update: refresh(bot, update, DELETE_COMPLETED_TORRENTS_MUTATION)
)

download_subtitles_handler = CommandHandler(
    'download_subtitles',
    lambda bot, update: refresh(bot, update, 'SUBTITLES')
)

download_not_found_movies_handler = CommandHandler(
    'download_not_found_movies',
    lambda bot, update: refresh(bot, update, SEARCH_MOVIES_MUTATION)
)

download_not_found_chapters_handler = CommandHandler(
    'download_not_found_chapters',
    lambda bot, update: refresh(bot, update, SEARCH_EPISODES_MUTATION)
)
