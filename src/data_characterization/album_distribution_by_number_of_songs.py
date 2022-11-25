from sys import argv
import matplotlib.pyplot as plt
import pandas as pd

filename = './processed/all.csv'

df = pd.read_csv(filename, sep=';')
data_by_album = df.groupby(['artist', 'album']).size()
print(data_by_album)
plt.hist(data_by_album, 20)
plt.title("Album distribution by number of songs")
plt.xlabel("Album mean track duration (min)")
plt.ylabel('# of albums')
plt.savefig('analysis/album_distribution_by_number_of_songs.svg')