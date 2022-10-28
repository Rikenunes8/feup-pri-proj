import pandas as pd
import os

filename = './processed/all.csv'
log_file = './data/log.txt'
lyrics_dir = './data/lyrics'

df = pd.read_csv(filename, sep=';')
df['normal_lyrics'] = df['lyrics'].str[12:]
log_df = pd.read_csv(log_file, sep=';')

tracks = df.groupby(['artist', 'track'], dropna=False).size()
lyric_files = os.listdir(lyrics_dir)

print('duplicated', len(tracks[lambda x: x ==2]))
print('general duplicated = ', tracks.sum() - tracks.count())

tracks_paths = df.value_counts('lyrics')

print(len(tracks_paths))


print(df.head(10))