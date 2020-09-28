#!/usr/bin/python
# -*- coding: UTF-8 -*-

import mysql.connector
from telegram import InlineQueryResultArticle, InputTextMessageContent, InputMediaPhoto, ParseMode, \
    InlineKeyboardMarkup, InlineKeyboardButton

config = {
    'user': 'amiuser',
    'password': 'ERT*&^8052kL',
    'host': '127.0.0.1',
    'database': 'amibroker',
    'raise_on_warnings': True
}


def inputTextMessageContent(last_deal, close, open, high, low, clock):
    message = '🔚<b>پایانی  </b>:{}\n\n'.format(close)
    message += '⬆<b>بیشترین </b>:{}\n\n'.format(high)
    message += '⬇<b>کمترین  </b>:{}\n\n'.format(low)
    message += '📈<b> آخرین  </b>:{}\n\n'.format(last_deal)
    message += '📉<b> اولین  </b>:{}\n\n'.format(open)
    message += '🕛️<b>آخرین اطلاعات قیمت</b>{}\n\n'.format(clock)
    # message += '{}\n\n'.format(img)
    message += '<b> کانال رسمی </b>️\n\n'

    return message


def get_data(var):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(dictionary=True)
    query = "SELECT c.*, p1.* FROM symboles c LEFT JOIN symboles_data p1 ON (c.id = p1.symbol_id) LEFT OUTER JOIN symboles_data p2 ON (c.id = p2.symbol_id AND (p1.date < p2.date OR (p1.date = p2.date AND p1.id_symbloes_data < p2.id_symbloes_data))) WHERE p2.id_symbloes_data IS NULL and  symbol LIKE %s LIMIT 50"
    cursor.execute(query, ('%' + var + '%',))
    symbol_list = cursor.fetchall()
    cursor.close()
    cnx.close()
    if not symbol_list:
        return
    results = list()
    keyboard = [[InlineKeyboardButton("وضعیت صف", callback_data='1'),
                 InlineKeyboardButton("حقیقی و حقوقی", callback_data='2')],

                [InlineKeyboardButton("کدال", callback_data='3')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    for symbol in symbol_list:
        # print(symbol)

        results.append(
            InlineQueryResultArticle(
                id=symbol['id'],
                title=symbol['symbol'],
                input_message_content=InputTextMessageContent(
                    inputTextMessageContent(symbol['last_deal'], symbol['close'], symbol['open'], symbol['high'],
                                            symbol['low'], symbol['time'])
                    , parse_mode=ParseMode.HTML,
                    disable_web_page_preview=False),
                description=symbol['name'],
                thumb_url='https://vpn.amibroker.ir/static/telbot/images/' + str(symbol['id']) + '.jpg',
                reply_markup=reply_markup
            )
        )
    return results


def get_symbol_data(var):
    ########################################
    # cnx = mysql.connector.connect(**config)
    # cursor = cnx.cursor(dictionary=True)
    # query = "SELECT * FROM symboles WHERE symbol LIKE %s LIMIT 50"
    # cursor.execute(query, (var + '%',))
    # symbol_list = cursor.fetchall()
    # cursor.close()
    # cnx.close()
    #
    # ind = [650000, 560000]
    # lgl = [10000, 90000]
    # if not ind:
    #     return
    # return [ind, lgl]
    ###########################################
    cell_text = [[2059564650, 55000, 2.74],
                 [207165460, -20000, -0.97],
                 # [19000, 150, 0.79],
                 # [20750, 710, 3.54],
                 # [20080, 180, 0.90],
                 ]
    return cell_text


def get_person_legal_statistic(symbol):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(dictionary=True)
    query = "SELECT `person_buy_volume`, `legal_buy_volume`, `person_sell_volume`,`legal_sell_volume`, `person_buy_count`, `legal_buy_count`, `person_sell_count`, `legal_sell_count` FROM symboles_data WHERE symbol_id=(SELECT id FROM symboles WHERE symbol LIKE %s)  ORDER BY id_symbol_data DESC LIMIT 1"
    cursor.execute(query, (symbol + '%',))
    symbol_data = cursor.fetchall()
    cursor.close()
    cnx.close()
    return symbol_data
