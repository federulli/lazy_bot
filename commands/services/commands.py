from decorators import admin_only
import subprocess


@admin_only
def services_status(bot, update):
    p = subprocess.run(
        ['sudo', 'supervisorctl', 'status'],
        stdout=subprocess.PIPE,
        shell=True
    )
    bot.send_message(
        chat_id=update.message.chat_id,
        text=p.stdout
    )

