import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from handlers import (greet_user, guess_number, send_cat_picture, user_coordinates, 
                      talk_to_me)
import settings

# PROXY = {'proxy_url': settings.PROXY_URL,
#          'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}
#          }

logging.basicConfig(filename='bot.log', format='%(asctime)s %(levelname)-8s %(message)s',level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

    
def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('guess', guess_number))
    dp.add_handler(CommandHandler('cat', send_cat_picture))
    dp.add_handler(MessageHandler(Filters.regex('^(Прислать кота)$'), send_cat_picture))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot started')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()
