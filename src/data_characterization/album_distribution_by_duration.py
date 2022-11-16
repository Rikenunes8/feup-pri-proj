from sys import argv
import matplotlib.pyplot as plt
import pandas as pd

filename = argv[1]

df = pd.read_csv(filename, sep=';')
albums_durations = df.groupby(['album', 'artist'])['track_duration (s)'].sum()
albums_durations = albums_durations.apply(lambda x: x/60).values
plt.hist(albums_durations, 20)
# title
plt.title('Album distribution by duration')
plt.xlabel('Album duration (min)')
plt.ylabel('# of albums')
plt.savefig('analysis/album_distribution_by_duration.svg')