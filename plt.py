import matplotlib.pyplot as plt
import numpy as np
from bidi.algorithm import get_display
from arabic_reshaper import reshape
import matplotlib
import uuid

from fetch_data import get_symbol_data

def plot_individual_legal(symbol):

    font = {"family": "BNazanin", "size": 14}
    matplotlib.rc("font", **font)

    t = np.arange(0., 5., 0.2)

    labels = ['خرید', 'فروش']
    persian_labels = [get_display(reshape(label)) for label in labels]

    [individual, legal] = get_symbol_data(symbol)

    men_std = [10000, 15000]
    women_std = [10000, 15000]
    width = 0.5
    # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()

    ax.bar(persian_labels, individual, width, yerr=men_std, label=get_display(reshape('حقیقی')))
    ax.bar(persian_labels, legal, width, yerr=women_std, bottom=individual,
           label=get_display(reshape('حقوقی')))

    ax.set_ylabel(get_display(reshape('تعداد سهام')))
    persian_title = get_display(reshape(symbol))
    ax.set_title(persian_title)
    ax.legend()
    ax.yaxis.set_major_formatter(matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))
    plt.tight_layout()
    # plt.show()
    file_name = str(uuid.uuid4())
    plt.savefig(file_name+'.png')
    return file_name+'.png'




    # x= .5; y=.5; plt.figtext(x, y, 'some text',)

    # Add a table at the bottom of the axes
    # data = [[ 66386, 174296,  75131, 577908,  32015],
    #         [ 58230, 381139,  78045,  99308, 160454],
    #         [ 89135,  80552, 152558, 497981, 603535],
    #         [ 78415,  81858, 150656, 193263,  69638],
    #         [139361, 331509, 343164, 781380,  52269]]
    #
    # cell_text = np.round(data, 3)
    # row_labels = ['r1','r2','r3','r4','r5']
    # col_labels = ['c1','c2','c3','c4','c5']

# kw = dict(cellColours=[["#EEECE1"] * len(data.iloc[0])] * len(data))  # to fill cells with color
# ytable = plt.table(cellText=cell_text, rowLabels=row_labels, colLabels=col_labels, loc="center right")
#     ytable = plt.table(cellText=cell_text, rowLabels=row_labels, colLabels=col_labels, loc="lower center")
# plt.subplots_adjust(left=0.2, bottom=0.2)
# plt.axis("off")
# plt.grid(False)


# the_table = plt.table(cellText='cell_text',
#                       rowLabels=row_labels,
#                       rowColours=colors,
#                       colLabels=col_labels,
#                       loc='bottom')
# plt.subplots_adjust(left=0.2, bottom=-10)

# value_increment = 1000
# values = np.arange(0, 2500, 500)
# plt.ylabel("Loss in ${0}'s".format(value_increment))
# plt.yticks(values * value_increment, ['%d' % val for val in values])
# plt.xticks([])
# plt.title('Loss by Disaster')


