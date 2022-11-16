from sys import argv
import matplotlib.pyplot as plt
import pandas as pd

filename = argv[1]

df = pd.read_csv(filename, sep=';')
durations_min = df['track_duration (s)'].apply(lambda x: x/60).values

plt.hist(durations_min, 30)
plt.title('Song distribution by duration')
plt.xlabel('Duration (min)')
plt.ylabel('# of tracks')
plt.savefig('analysis/song_distribution_by_duration.png')

plt.figure()
plt.yscale('log')
plt.hist(durations_min, 30)
plt.title('Song distribution by duration (log)')
plt.xlabel('Duration (min)')
plt.ylabel('# of tracks')
plt.savefig('analysis/song_distribution_by_duration_log.png')