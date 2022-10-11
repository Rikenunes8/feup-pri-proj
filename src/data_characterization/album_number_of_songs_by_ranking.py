from sys import argv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filename = argv[1]

def aggr_func(data):
    return pd.Series({
        'number_of_songs': data['n_tracks'].iat[0],
        'ranking':  data['album_ranking'].iat[0]
    })


df = pd.read_csv(filename, sep=';')
album_data = df.groupby(['album', 'artist']).apply(aggr_func)
album_data_sort = album_data.sort_values('ranking')

x = album_data_sort['ranking']
y = album_data_sort['number_of_songs']
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

plt.scatter(x, y)
plt.plot(x,p(x),"r--")
plt.xlabel('Ranking')
plt.ylabel('# of tracks by album')

plt.savefig('analysis/album_number_of_songs_by_ranking.png')
