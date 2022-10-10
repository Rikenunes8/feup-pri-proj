from sys import argv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filename = './processed/all.csv'


def aggr_func(data):
    return pd.Series({
        'number_of_songs': len(data.index),
        'ranking':  data['ranking'].iat[0]
    })


df = pd.read_csv(filename, sep=';')
album_data = df.groupby(['album', 'artist']).apply(aggr_func)
album_data_sort = album_data.sort_values('ranking')

x = album_data_sort['ranking']
y = album_data_sort['number_of_songs']

plt.scatter(x, y)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")

album_data.sort_values('number_of_songs').head(10)
plt.show()

# plt.savefig('./analysis/album_number_of_songs_by_ranking.png')
