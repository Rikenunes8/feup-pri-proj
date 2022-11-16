from sys import argv
import matplotlib.pyplot as plt
import pandas as pd

filename = argv[1]

df = pd.read_csv(filename, sep=";")

df_group = df.groupby('album')['album_release_date'].max()

plt.hist(df_group, range(1935, 2025, 5))
plt.title("Album distribution by year")
plt.xlabel('Album release date')
plt.ylabel('# of albums')
plt.savefig('analysis/album_distribution_by_year.svg')
