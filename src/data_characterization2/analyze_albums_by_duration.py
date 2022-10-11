from sys import argv
import matplotlib.pyplot as plt
import pandas as pd

filename = argv[1]

df = pd.read_csv(filename, sep=';')

df_group = df.groupby('album')['track_duration (s)'].sum()

plt.hist(df_group.apply(lambda x: x/60).values, 20)
plt.xlabel('Album duration (min)')
plt.ylabel('# of albums')
plt.savefig('analysis/albums_by_duration.png')
