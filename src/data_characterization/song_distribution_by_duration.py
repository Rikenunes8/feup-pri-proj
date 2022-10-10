from sys import argv
import matplotlib.pyplot as plt
import pandas as pd

filename = argv[1]

df = pd.read_csv(filename, sep=';')
plt.hist(df['track_duration (s)'].values, 30, rwidth=0.9)
plt.savefig('analysis/song_distribution_by_duration.png')
plt.yscale('log', nonposy='clip')
plt.hist(df['track_duration (s)'].values, 30, rwidth=0.9, )
plt.savefig('analysis/song_distribution_by_duration_log.png')