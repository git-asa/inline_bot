from telegram.ext import Updater
import logging
from telegram.ext import InlineQueryHandler
from fetch_data import get_data
import time


updater = Updater(token='1384477475:AAE2RYA7H-6kjXTY7B7XQwgRTMQ83arLwB0', use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def inline_symbol(update, context):
    var = update.inline_query.query
    # if len(var) > 1:
    results = get_data(var)
    context.bot.answer_inline_query(update.inline_query.id, results, cache_time=10)


inline_symbol_handler = InlineQueryHandler(inline_symbol)
dispatcher.add_handler(inline_symbol_handler)
############################vahid

# def echo(update, context):
#     for x in range(47,49):
#         try:
#             time.sleep(1)
#             # print('https://vpn.amibroker.ir/static/telbot/images/'+str(x)+'.jpg')
#             context.bot.send_photo(chat_id=update.effective_chat.id, caption= str(x), photo='https://vpn.amibroker.ir/static/telbot/images/'+str(x)+'.jpg')
#         except AssertionError as error:
#             print(error)
#             print(str(x))


from telegram.ext import MessageHandler, Filters
# echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
# ###########################vahid
# dispatcher.add_handler(echo_handler)
updater.start_polling()
