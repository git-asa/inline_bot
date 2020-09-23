from telegram.ext import Updater
updater = Updater(token='1384477475:AAE2RYA7H-6kjXTY7B7XQwgRTMQ83arLwB0', use_context=True)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def test(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="this is from test")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
# updater.start_webhook(listen='0.0.0.0',
#                       port=443,
#                       url_path='TOKEN',
#                       key='private.key',
#                       cert='cert.pem',
#                       webhook_url='https://example.com:443/1384477475:AAE2RYA7H-6kjXTY7B7XQwgRTMQ83arLwB0')

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
print('test')
from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)
