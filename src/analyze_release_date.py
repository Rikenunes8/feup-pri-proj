from sys import argv
import matplotlib.pyplot as plt
import pandas as pd

filename = argv[1]

df = pd.read_csv(filename, sep=';')
plt.hist(df['album_release_date'].values, 10, rwidth=0.9)
plt.savefig('analysis/tracks_realeses_hist.png')
