from sys import argv
import matplotlib.pyplot as plt
import pandas as pd

filename = './processed/all.csv'

df = pd.read_csv(filename, sep=';')
data_by_album = df.groupby(['album', 'artist'])
sum_data_by_album = data_by_album.aggregate('sum')
plt.hist(sum_data_by_album['track_duration (s)'].values, 20, rwidth=0.9)
plt.savefig('./analysis/album_distribution_by_duration.png')