from telegram.ext import (
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    Filters,
)

from commands.tvshow.commands import (
    add_tv_show,
    create_tv_show,
    add_season,
    create_season,
    read_tv_show_id,
    cancel,
)
from commands.tvshow.status import (
    CREATE_TV_SHOW,
    READ_TV_SHOW_ID,
    CREATE_SEASON,
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
