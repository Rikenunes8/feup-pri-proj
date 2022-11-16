from sys import argv
import matplotlib.pyplot as plt
import pandas as pd

filename = './processed/all.csv'

df = pd.read_csv(filename, sep=';')
data_by_album = df.groupby(['album', 'artist'])['track_duration (s)'].mean()
albums_means = data_by_album.apply(lambda x: x / 60).values

plt.hist(albums_means, 20)
plt.title("Album distribution by mean song duration")
plt.xlabel("Album mean track duration (min)")
plt.ylabel('# of albums')
plt.savefig('analysis/album_distribution_by_mean_song_duration.png')