from sys import argv
import matplotlib.pyplot as plt
import pandas as pd

filename = argv[1]

df = pd.read_csv(filename, sep=';')
plt.hist(df['track_duration (s)'].apply(lambda x: x/60).values, 20)
plt.xlabel('Track duration (min)')
plt.ylabel('# of tracks')
plt.savefig('analysis/tracks_by_duration.png')
