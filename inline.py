from telegram.ext import Updater
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import InlineQueryHandler, CallbackQueryHandler, CommandHandler
from fetch_data import get_data
import time


updater = Updater(token='1136825228:AAHN4Gbt-pZG5OP3QNyLKGIAgcTzmgqYh24', use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

#
# def inline_symbol(update, context):
#     var = update.inline_query.query
#     # if len(var) > 1:
#     results = get_data(var)
#     context.bot.answer_inline_query(update.inline_query.id, results, cache_time=10)
#
#
# inline_symbol_handler = InlineQueryHandler(inline_symbol)
#
# dispatcher.add_handler(inline_symbol_handler)



def button(update, context):
    query = update.callback_query

    query.answer()

    # query.edit_message_text(text="Selected option: {}".format(query.data))


def button1(update, context):
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    query.edit_message_text(text="Selected option: {}".format(query.data))

updater.dispatcher.add_handler(CallbackQueryHandler(button))




def start(update, context):
    keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
                 InlineKeyboardButton("Option 2", callback_data='2')],

                [InlineKeyboardButton("Option 3", callback_data='3')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)
updater.dispatcher.add_handler(CommandHandler('start', start))
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


# from telegram.ext import MessageHandler, Filters
# echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
# ###########################vahid
# dispatcher.add_handler(echo_handler)
updater.start_polling()
