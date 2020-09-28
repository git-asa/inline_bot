import datetime
import mysql.connector
import matplotlib
from bidi.algorithm import get_display
from arabic_reshaper import reshape
import numpy as np
import plotly.graph_objects as go
import uuid
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


class Symbol:
    def __init__(self, symbol):
        self.symbol = symbol
        self.last_deal = 0
        self.close = 0
        self.open = 0
        self.close_yesterday = 0
        self.high = 0
        self.low = 0
        self.deal_count = 0
        self.volume = 0
        self.value = 0
        self.date = datetime.date.today()
        self.person_buy_volume = 0
        self.legal_buy_volume = 0
        self.person_sell_volume = 0
        self.legal_sell_volume = 0
        self.person_buy_count = 0
        self.legal_buy_count = 0
        self.person_sell_count = 0
        self.legal_sell_count = 0
        self.count_buy_total = self.person_buy_count + self.legal_buy_count
        self.count_sell_total = self.person_sell_count + self.legal_sell_count


    def close_status(self):
        if self.close_yesterday:
            return {"close": self.close, "difference": self.close - self.close_yesterday,
                    "percentage": (self.close / self.close_yesterday - 1) * 100}

    def last_deal_status(self):
        if self.close_yesterday:
            return {"last_deal": self.last_deal, "difference": self.last_deal - self.close_yesterday,
                    "percentage": (self.last_deal / self.close_yesterday - 1) * 100}

    # def general_draw(self, coordinates, elements,**kwargs):
    #     x = 45
    #     y = 70
    #     # this was a 400x400 jpg file
    #     imageFile = "kolli.png"
    #     image = Image.open(imageFile)
    #     # first you must prepare your text (you dont need this step for english text)
    #     # start drawing on image
    #     # row 1 last
    #     draw = ImageDraw.Draw(image)
    #     for value in elements.values():
    #         draw.text(elements[], value, (0,0,0))
    #
    #
    #     draw.text((x, y), str(round(self.difference_close_percent, 2)),
    #               (44, 194, 44) if self.difference_close > 0 else (255, 0, 0), font=font)
    #     draw.text((x + 190, y), str(self.difference_close), (44, 194, 44) if self.difference_close > 0 else (255, 0, 0),
    #               font=font)
    #     draw.text((x + 365, y), str(self.close), (0, 0, 0), font=font)
    #     # row 2 lasted
    #     draw.text((x, y + 55), str(round(self.difference_last_deal_percent, 2)),
    #               (44, 194, 44) if self.difference_last_deal > 0 else (255, 0, 0), font=font)
    #     draw.text((x + 190, y + 55), str(self.difference_last_deal),
    #               (44, 194, 44) if self.difference_last_deal > 0 else (255, 0, 0), font=font)
    #     draw.text((x + 365, y + 55), str(self.last_deal), (0, 0, 0), font=font)
    #     ImageDraw.Draw(image)
    #     file_name = str(uuid.uuid4()) + '.png'
    #     image.save(file_name)
    #     return file_name


class SymbolData(Symbol):
    def __init__(self, symbol, config):
        if symbol:
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor(dictionary=True)
            query = "SELECT * FROM symboles_data WHERE symbol_id=(SELECT id FROM symboles WHERE symbol LIKE %s)  ORDER BY id_symbol_data DESC LIMIT 1"
            cursor.execute(query, (symbol + '%',))
            symbol_data = cursor.fetchall()
            cursor.close()
            cnx.close()

            self.symbol = symbol
            self.id_symbol_data = symbol_data[0].get('id_symbol_data')
            self.symbol_id = symbol_data[0].get('symbol_id')
            self.last_deal = symbol_data[0].get('last_deal')
            self.close = symbol_data[0].get('close')
            self.open = symbol_data[0].get('open')
            self.close_yesterday = symbol_data[0].get('close_yesterday')
            self.high = symbol_data[0].get('high')
            self.low = symbol_data[0].get('low')
            self.deal_count = symbol_data[0].get('deal_count')
            self.volume = symbol_data[0].get('volume')
            self.value = symbol_data[0].get('value')
            self.date = symbol_data[0].get('date')
            self.person_buy_volume = symbol_data[0].get('person_buy_volume')
            self.legal_buy_volume = symbol_data[0].get('legal_buy_volume')
            self.person_sell_volume = symbol_data[0].get('person_sell_volume')
            self.legal_sell_volume = symbol_data[0].get('legal_sell_volume')
            self.person_buy_count = symbol_data[0].get('person_buy_count')
            self.legal_buy_count = symbol_data[0].get('legal_buy_count')
            self.person_sell_count = symbol_data[0].get('person_sell_count')
            self.legal_sell_count = symbol_data[0].get('legal_sell_count')
            self.difference_close = self.close - self.close_yesterday
            self.difference_close_percent = (self.close/self.close_yesterday -1 ) * 100
            self.difference_last_deal = self.last_deal - self.close_yesterday
            self.difference_last_deal_percent = (self.last_deal/self.close_yesterday - 1) * 100

    def close_status_list(self):
        return list(self.close_status().values())

    def last_deal_status_list(self):
        return list(self.last_deal_status().values())

    def close_last_deal_status(self):
        return [self.close_status_list(), self.last_deal_status_list()]

    # def general_draw(self, **kwargs):

        # x = 45 if 'x' not in kwargs.keys() else x = kwargs.get('x')
        # y = 70 if 'x' not in kwargs.keys() else y = kwargs.get('x')
        # if
        # for i in coordinates:
        #     i

    def general_info(self):
        # import pdb;
        # pdb.set_trace()
        font = {"family": "BNazanin", "size": 14}
        matplotlib.rc("font", **font)

        row_labels = ['پایانی', 'آخرین']
        # row_labels = [ 'بیشترین', 'کمترین', 'اولین',]
        persian_row_labels = [get_display(reshape(label)) for label in row_labels]

        col_labels = ['قیمت', 'تغییر', 'درصد']
        persian_col_labels = [get_display(reshape(label)) for label in col_labels]

        #
        cell_text = self.close_last_deal_status()
        vectorized_cell_text = np.vectorize(lambda i: "{:,}".format(i))
        cell_text_str_comma_seprated = vectorized_cell_text(cell_text)

        fig = go.Figure(data=[go.Table(
            header=dict(values=col_labels,
                        line_color='darkslategray',
                        fill_color='lightskyblue',
                        align='left'),
            cells=dict(values=np.array(cell_text_str_comma_seprated).transpose(),  # 2nd column
                       line_color='darkslategray',
                       fill_color='lightcyan',
                       align='left'))
        ])
        fig.update_layout(
            autosize=False,
            width=350,
            height=120,
            margin=dict(l=20, r=20, b=20, t=20, pad=4), )

        file_name = str(uuid.uuid4())
        fig.write_image(file_name + '.png')
        return file_name

    def general_info_draw(self):  # , Coordinates
        x = 45; y = 70
        # use a good font!
        fontFile = "B-NAZANIN.TTF"

        # this was a 400x400 jpg file
        imageFile = "kolli.png"

        # load the font and image
        font = ImageFont.truetype(fontFile, 30)
        image = Image.open(imageFile)

        # first you must prepare your text (you dont need this step for english text)

        # tmp = self.close
        # vectorized_cell_text = np.vectorize(lambda i: "{:,}".format(i))
        # tmp_txt = vectorized_cell_text(tmp)

        # start drawing on image
        # row 1 last
        draw = ImageDraw.Draw(image)
        draw.text((x, y), str(round(self.difference_close_percent,2)), (44, 194, 44) if self.difference_close > 0 else (255, 0, 0), font=font)
        draw.text((x + 190, y), str(self.difference_close), (44, 194, 44) if self.difference_close > 0 else (255, 0, 0), font=font)
        draw.text((x + 365, y), str(self.close), (0, 0, 0), font=font)
        # row 2 lasted
        draw.text((x, y + 55), str(round(self.difference_last_deal_percent,2)), (44, 194, 44) if self.difference_last_deal > 0 else (255, 0, 0), font=font)
        draw.text((x + 190, y + 55), str(self.difference_last_deal), (44, 194, 44) if self.difference_last_deal > 0 else (255, 0, 0), font=font)
        draw.text((x + 365, y + 55), str(self.last_deal), (0, 0, 0), font=font)
        ImageDraw.Draw(image)
        file_name = str(uuid.uuid4()) + '.png'
        image.save(file_name)
        return file_name