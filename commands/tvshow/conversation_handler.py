from telegram.ext import (
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    Filters,
)

from commands.tvshow.commands.create_season import (
    create_season,
    add_season,
    read_tv_show_id,
)

from commands.tvshow.commands.create_tv_show import (
    add_tv_show,
    create_tv_show,
)

from commands.tvshow.commands.list_tv_shows import list_tv_shows

from commands.tvshow.commands.list_seasons import (
    list_seasons,
    get_seasons
)
from ..utils import cancel

from commands.tvshow.status import (
    CREATE_TV_SHOW,
    READ_TV_SHOW_ID,
    CREATE_SEASON,
    LIST_SEASONS,
)

tv_show_conversation_handler = ConversationHandler(
    entry_points=[
        CommandHandler('add_tv_show', add_tv_show)
    ],
    states={
        CREATE_TV_SHOW: [
            MessageHandler(
                Filters.text,
                create_tv_show,
                pass_chat_data=True
            )
        ]
    },
    fallbacks=[
        CommandHandler('cancel', cancel)
    ]
)

season_conversation_handler = ConversationHandler(
    entry_points=[
        CommandHandler('add_season', add_season)
    ],
    states={
        READ_TV_SHOW_ID: [
            MessageHandler(
                Filters.text,
                read_tv_show_id,
                pass_chat_data=True
            )
        ],
        CREATE_SEASON: [
            MessageHandler(
                Filters.text,
                create_season,
                pass_chat_data=True
            )
        ]
    },
    fallbacks=[
        CommandHandler('cancel', cancel)
    ]
)

list_tv_shows_handler = CommandHandler(
    'list_tv_shows',
    list_tv_shows
)

list_seasons_conversation_handler = ConversationHandler(
    entry_points=[
        CommandHandler('list_seasons', list_seasons)
    ],
    states={
        LIST_SEASONS: [
            MessageHandler(
                Filters.text,
                get_seasons,
                pass_chat_data=True
            )
        ]
    },
    fallbacks=[
        CommandHandler('cancel', cancel)
    ]
)
