import requests
from ..utils import get_host
from tabulate import tabulate


def add_tv_show(bot, update, **kwargs):
    if not kwargs.get('args'):
        bot.send_message(
            chat_id=update.message.chat_id,
            text="TV Show name missing"
        )
        return
    name = " ".join(kwargs['args'])
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


def list_tv_shows(bot, update):
    r = requests.get(
        '{}/tv-shows/'.format(get_host())
    )
    bot.send_message(
        chat_id=update.message.chat_id,
        text='`{}`'.format(
            tabulate([[tv_show['name'], tv_show['id']] for tv_show in r.json()], headers=['name', 'id'])
        ),
    )


def add_season(bot, update, **kwargs):
    if len(kwargs.get('args', [])) != 2:
        bot.send_message(
            chat_id=update.message.chat_id,
            text='`/add_season <tv-show-id> <season_number>`'
        )
        return
    r = requests.post(
        "{}/tv-shows/{}/seasons/".format(get_host(), kwargs['args'][0]),
        json={"number": kwargs['args'][1]}
    )
    bot.send_message(
        chat_id=update.message.chat_id,
        text=r.status_code
    )
