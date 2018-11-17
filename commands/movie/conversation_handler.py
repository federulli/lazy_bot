from telegram.ext import (
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    Filters,
)

from commands.movie.commands import (
    add_movie,
    create_movie,
    cancel,
)
from commands.movie.status import (
    CREATE_MOVIE,
)

movie_conversation_handler = ConversationHandler(
    entry_points=[
        CommandHandler('add_movie', add_movie)
    ],
    states={
        CREATE_MOVIE: [
            MessageHandler(
                Filters.text,
                create_movie,
                pass_chat_data=True
            )
        ]
    },
    fallbacks=[
        CommandHandler('cancel', cancel)
    ]
)
