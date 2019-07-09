from pprint import pprint
from telegram.ext import Updater, CommandHandler

import settings


def hello_user(bot, update):
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name

    update.message.reply_text(f'Привет, {first_name} {last_name}!')

    pprint(update.message.from_user.__dict__)


def main():
    my_bot = Updater(settings.TOKEN, request_kwargs={
        'proxy_url': settings.SOCKS_PROXY
    })
    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler('start', hello_user))

    my_bot.start_polling()
    my_bot.idle()


if __name__ == '__main__':
    main()
