from sys import argv
import matplotlib.pyplot as plt
import pandas as pd

filename = argv[1]

df = pd.read_csv(filename, sep=';')
hasnot = df['lyrics'].isna().sum()
has = df['lyrics'].shape[0] - hasnot

plt.bar(['has', 'has not'], [has, hasnot], color ='maroon', width = 0.4)
plt.savefig('analysis/tracks_lyrics_existence.png')