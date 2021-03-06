from telegram.ext import (
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    Filters,
)

from commands.movie.commands import (
    add_movie,
    read_movie_name,
    create_movie,
    cancel,
    list_movies,
)
from commands.movie.status import (
    READ_MOVIE_NAME,
    CREATE_MOVIE,
)

movie_conversation_handler = ConversationHandler(
    entry_points=[
        CommandHandler('add_movie', add_movie)
    ],
    states={
        READ_MOVIE_NAME: [
            MessageHandler(
                Filters.text,
                read_movie_name,
                pass_chat_data=True
            )
        ],
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

list_movies_handler = CommandHandler(
    'list_movies',
    list_movies
)
