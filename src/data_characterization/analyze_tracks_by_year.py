from sys import argv
import matplotlib.pyplot as plt
import pandas as pd

filename = argv[1]

df = pd.read_csv(filename, sep=';')
plt.hist(df['album_release_date'].values, range(1935, 2025, 5))
plt.xlabel('Track release date')
plt.ylabel('# of tracks')
plt.savefig('analysis/tracks_by_year.png')
