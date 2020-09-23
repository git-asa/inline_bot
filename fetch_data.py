#!/usr/bin/python
# -*- coding: UTF-8 -*-

import mysql.connector
from telegram import InlineQueryResultArticle, InputTextMessageContent, InputMediaPhoto, ParseMode

config = {
    'user': 'root',
    'password': '1234',
    'host': '127.0.0.1',
    'database': 'amibroker',
    'raise_on_warnings': True
}


def inputTextMessageContent(last_deal, close, open, high, low, clock,img):
    message = '🔚<b>پایانی  </b>:{}\n\n'.format(close)
    message += '⬆<b>بیشترین </b>:{}\n\n'.format(high)
    message += '⬇<b>کمترین  </b>:{}\n\n'.format(low)
    message += '📈<b> آخرین  </b>:{}\n\n'.format(last_deal)
    message += '📉<b> اولین  </b>:{}\n\n'.format(open)
    message += '🕛️<b>آخرین اطلاعات قیمت</b>{}\n\n'.format(clock)
    message += '{}\n\n'.format(img)
    message += '<b> کانال رسمی </b>️\n\n'

    return message


def get_data(var):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(dictionary=True)
    query = "SELECT c.*, p1.* FROM symboles c JOIN symboles_data p1 ON (c.id = p1.symbol_id) LEFT OUTER JOIN symboles_data p2 ON (c.id = p2.symbol_id AND (p1.date < p2.date OR (p1.date = p2.date AND p1.id < p2.id))) WHERE p2.id IS NULL and  symbol LIKE %s LIMIT 50"
    cursor.execute(query, (var + '%',))
    symbol_list = cursor.fetchall()
    cursor.close()
    cnx.close()
    if not symbol_list:
        return
    results = list()
    for symbol in symbol_list:
        results.append(
            InlineQueryResultArticle(
                id=symbol['id'],
                title=symbol['symbol'],
                input_message_content=InputTextMessageContent(message_text='twsr',parse_mode=ParseMode.HTML,disable_web_page_preview=False),
                description=symbol[2],
                thumb_url='https://vpn.amibroker.ir/static/telbot/images/' + str(symbol['id']) + '.jpg'
            )
        )
    return results

def get_symbol_data(var):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(dictionary=True)
    query = "SELECT * FROM symboles WHERE symbol LIKE %s LIMIT 50"
    cursor.execute(query, (var + '%',))
    symbol_list = cursor.fetchall()
    cursor.close()
    cnx.close()

    ind = [650000, 560000]
    lgl = [10000, 90000]
    if not ind:
        return
    return [ind, lgl]
