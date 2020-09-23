import numpy as np
import matplotlib.pyplot as plt

from plt import plot_individual_legal

# ind = [650000, 560000]
# lgl = [10000, 90000]
p = plot_individual_legal('پکرمان')



import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import re

#########################################################
# data = [[ 66386, 174296,  75131, 577908,  32015],
#         [ 58230, 381139,  78045,  99308, 160454],
#         [ 89135,  80552, 152558, 497981, 603535],
#         [ 78415,  81858, 150656, 193263,  69638],
#         [139361, 331509, 343164, 781380,  52269]]
#
# columns = ('Freeze', 'Wind', 'Flood', 'Quake', 'Hail')
# rows = ['%d year' % x for x in (100, 50, 20, 10, 5)]
#
# values = np.arange(0, 2500, 500)
# value_increment = 1000
#
# # Get some pastel shades for the colors
# colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
# n_rows = len(data)
#
# index = np.arange(len(columns)) + 0.3
# bar_width = 0.4
#
# # Initialize the vertical-offset for the stacked bar chart.
# y_offset = np.zeros(len(columns))
#
# # Plot bars and create text labels for the table
# cell_text = []
# for row in range(n_rows):
#     plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
#     y_offset = y_offset + data[row]
#     cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])
# # Reverse colors and text labels to display the last value at the top.
# colors = colors[::-1]
# cell_text.reverse()
#
# # Add a table at the bottom of the axes
# the_table = plt.table(cellText=cell_text,
#                       rowLabels=rows,
#                       rowColours=colors,
#                       colLabels=columns,
#                       loc='bottom')
#
# # Adjust layout to make room for the table:
# plt.subplots_adjust(left=0.2, bottom=0.2)
#
# plt.ylabel("Loss in ${0}'s".format(value_increment))
# plt.yticks(values * value_increment, ['%d' % val for val in values])
# plt.xticks([])
# plt.title('Loss by Disaster')
#
# plt.show()
###############################################################
##

########################################
# xvals = [i for i in range(0, 10)]
# yvals1 = [i**2 for i in range(0, 10)]
# xvals2 = list(np.array(xvals) * 10)
# yvals2 = [i**3 for i in range(0, 10)]
#
# f, ax = plt.subplots(1)
# ax.plot(xvals, yvals1)
# ax.plot(xvals2, yvals2)
#######################################

#######################################
# x = np.linspace(0, 2 * np.pi, 400)
# y = np.sin(x ** 2)
#
# fig, axs = plt.subplots(1,3)
# fig.suptitle('Vertically stacked subplots')
# axs[0].plot(x, y)
# axs[1].plot(x, -y)
#######################################
# plt.show()

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/Mining-BTC-180.csv")

for i, row in enumerate(df["Date"]):
    p = re.compile(" 00:00:00")
    datetime = p.split(df["Date"][i])[0]
    df.iloc[i, 1] = datetime

fig = make_subplots(
    rows=3, cols=1,
    shared_xaxes=True,
    vertical_spacing=0.03,
    specs=[[{"type": "table"}],
           [{"type": "scatter"}],
           [{"type": "scatter"}]]
)

fig.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["Mining-revenue-USD"],
        mode="lines",
        name="mining revenue"
    ),
    row=3, col=1
)

fig.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["Hash-rate"],
        mode="lines",
        name="hash-rate-TH/s"
    ),
    row=2, col=1
)

fig.add_trace(
    go.Table(
        header=dict(
            values=["Date", "Number<br>Transactions", "Output<br>Volume (BTC)",
                    "Market<br>Price", "Hash<br>Rate", "Cost per<br>trans-USD",
                    "Mining<br>Revenue-USD", "Trasaction<br>fees-BTC"],
            font=dict(size=10),
            align="left"
        ),
        cells=dict(
            values=[df[k].tolist() for k in df.columns[1:]],
            align = "left")
    ),
    row=1, col=1
)
fig.update_layout(
    height=800,
    showlegend=False,
    title_text="Bitcoin mining stats for 180 days",
)

fig.show()
