import matplotlib.pyplot as plt
import pandas as pd
from sys import argv

filename = argv[1]

df = pd.read_csv(filename, sep=';')

df_groupby = df.groupby('album')[['track_duration (s)', 'album_release_date', 'album_ranking']].mean()

x = df_groupby['album_release_date'].apply(lambda x: int(x))
y = df_groupby['track_duration (s)'].apply(lambda x: x/60)
t = df_groupby['album_ranking'].apply(lambda x: int(round(x, 0)))

plt.figure(figsize=[10, 6.4])
plt.scatter(x, y, c=t, cmap='viridis')
plt.xlabel('Album release date')
plt.ylabel('Album tracks mean duration (min)')
cbar = plt.colorbar()
cbar.set_label('Album ranking', rotation=270, labelpad=20)

plt.savefig('analysis/album_ranking_by_release_and_mean_duration.png')
