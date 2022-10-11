from sys import argv
import matplotlib.pyplot as plt
import pandas as pd

filename = argv[1]

df = pd.read_csv(filename, sep=';')
data_by_album = df.groupby(['album', 'artist'])
data_by_album_first = data_by_album.first()
plt.hist(data_by_album_first['album_release_date'].values, 10, rwidth=0.9)
plt.xlabel('Album release date')
plt.ylabel('# of albums')
plt.savefig('analysis/album_distribution_by_year.png')