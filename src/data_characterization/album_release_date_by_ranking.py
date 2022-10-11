from sys import argv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filename = argv[1]


def aggr_func(data):
    return pd.Series({
        'ranking': data['album_rank'].iat[0],
        'album_release_date':  data['album_release_date'].iat[0]
    })


df = pd.read_csv(filename, sep=';')
album_data = df.groupby(['album', 'artist']).apply(aggr_func)
album_data_sort = album_data.sort_values('ranking')

x = album_data_sort['ranking']
y = album_data_sort['album_release_date']
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

plt.scatter(x, y)
plt.plot(x,p(x),"r--")
plt.xlabel('Ranking')
plt.ylabel('Album release date')

plt.savefig('analysis/album_release_date_by_ranking.png')
