from sys import argv
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Rectangle

filename = argv[1]

df = pd.read_csv(filename, sep=";")

df_group = df.groupby('album')['album_release_date'].max()

plt.hist(df['album_release_date'], range(1935, 2025, 5))
plt.hist(df_group, range(1935, 2025, 5))
handles = [Rectangle((0, 0), 1, 1, color=c, ec="k") for c in ['C0', 'C1']]
plt.legend(handles, ['Tracks', 'Albums'])
plt.xlabel('Release date')
plt.savefig('analysis/albums_and_tracks_by_year.png')
