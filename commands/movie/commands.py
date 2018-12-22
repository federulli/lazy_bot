import requests
from ..utils import get_host
from decorators import admin_only

from commands.movie.status import (
    READ_MOVIE_NAME,
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
    return READ_MOVIE_NAME


def read_movie_name(bot, update, chat_data):
    chat_data['name'] = update.message.text
    update.message.reply_text(
        'Ingrese el anio de la pelicula, 0 si no se sabe:\n'
    )
    return CREATE_MOVIE


def create_movie(bot, update, chat_data):
    name = chat_data['name']
    try:
        # todo algun dia hacer esto bien
        year = int(update.message.text)
        if year <= 0:
            raise Exception()
    except:
        year = None

    new_movie = {
        "name": name,
        "year": year
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
    message = ("id: {}\nname: {}\nyear: {}\nfound: {}".format(
        movie['id'], movie['name'], movie.get('year', ''),
        movie['torrent'] is not None
    ) for movie in r.json())
    bot.send_message(
        chat_id=update.message.chat_id,
        text='\n\n'.join(
          message
        ),
        parse_mode='markdown'
    )
