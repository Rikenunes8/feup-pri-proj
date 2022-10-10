from sys import argv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filename = './processed/all.csv'


def aggr_func(data):
    return pd.Series({
        'album_duration': data['track_duration (s)'].sum(),
        'ranking':  data['ranking'].iat[0]
    })


df = pd.read_csv(filename, sep=';')
album_data = df.groupby(['album', 'artist']).apply(aggr_func)
album_data_sort = album_data.sort_values('ranking')

x = album_data_sort['ranking']
y = album_data_sort['album_duration']

plt.scatter(x, y)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")

# plt.show()
plt.savefig('./analysis/album_duration_by_ranking.png')
