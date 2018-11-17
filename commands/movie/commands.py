import requests
from ..utils import get_host
from tabulate import tabulate
from decorators import admin_only

from commands.movie.status import (
    CREATE_MOVIE,
    END,
)


def cancel(bot, update):
    update.effective_message.reply_text('Operación cancelada')
    return END


@admin_only
def add_movie(bot, update):
    update.message.reply_text(
        'Ingrese el nombre de la pelicula:\n'
    )
    return CREATE_MOVIE


def create_movie(bot, update, chat_data):
    name = update.message.text
    new_movie = {
        "name": name
    }
    r = requests.post(
        '{}/movies/'.format(get_host()),
        json=new_movie
    )
    bot.send_message(
        chat_id=update.message.chat_id,
        text="{} id: {}".format(name, r.json()['id'])
    )
    return END


@admin_only
def list_movies(bot, update):
    r = requests.get(
        '{}/movies/'.format(get_host())
    )
    bot.send_message(
        chat_id=update.message.chat_id,
        text='```{}```'.format(
            tabulate([[movie['name'], movie['id']] for movie in r.json()])
        ),
        parse_mode='markdown'
    )
