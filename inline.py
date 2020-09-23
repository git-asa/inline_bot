#git
from telegram.ext import Updater
import logging
from telegram.ext import InlineQueryHandler
from fetch_data import get_data, get_symbol_data
from plt import plot_individual_legal

updater = Updater(token='1384477475:AAE2RYA7H-6kjXTY7B7XQwgRTMQ83arLwB0', use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def inline_symbol(update, context):
    var = update.inline_query.query
    if len(var) > 1:
        results = get_data(var)
        ##
        plot_individual_legal('پکرمان')
        ##
        context.bot.answer_inline_query(update.inline_query.id, results)


inline_symbol_handler = InlineQueryHandler(inline_symbol)
dispatcher.add_handler(inline_symbol_handler)

updater.start_polling()
