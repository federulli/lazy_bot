import requests
from ..utils import get_host
from tabulate import tabulate


from commands.tvshow.status import (
    CREATE_TV_SHOW,
    READ_TV_SHOW_ID,
    CREATE_SEASON,
    END,
)


def cancel(bot, update):
    update.effective_message.reply_text('Operación cancelada')
    return END


def add_tv_show(bot, update):
    update.message.reply_text(
        'Ingrese el nombre de la serie:\n'
    )
    return CREATE_TV_SHOW


def create_tv_show(bot, update, chat_data):
    name = update.message.text
    new_tv_show = {
        "name": name
    }
    r = requests.post(
        '{}/tv-shows/'.format(get_host()),
        json=new_tv_show
    )
    bot.send_message(
        chat_id=update.message.chat_id,
        text="{} id: {}".format(name, r.json()['id'])
    )
    return END


def list_tv_shows(bot, update):
    r = requests.get(
        '{}/tv-shows/'.format(get_host())
    )
    bot.send_message(
        chat_id=update.message.chat_id,
        text='```{}```'.format(
            tabulate([[tv_show['name'], tv_show['id']] for tv_show in r.json()])
        ),
        parse_mode='markdown'
    )


def add_season(bot, update):
    update.message.reply_text(
        'Ingrese el id de la serie:\n'
    )
    return READ_TV_SHOW_ID


def read_tv_show_id(bot, update, chat_data):
    chat_data['tv_show_id'] = update.message.text
    update.message.reply_text(
        'Ingrese la nueva temporada:\n'
    )
    return CREATE_SEASON


def create_season(bot, update, chat_data):
    r = requests.post(
        "{}/tv-shows/{}/seasons/".format(
            get_host(),
            chat_data['tv_show_id']
        ),
        json={"number": update.message.text}
    )
    bot.send_message(
        chat_id=update.message.chat_id,
        text=r.status_code
    )
    return END
