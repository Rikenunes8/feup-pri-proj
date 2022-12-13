import pandas as pd
import sys
from lyrics_extractor import SongLyrics
from os import chdir
import os
from dotenv import load_dotenv
from utils import normalize_lyrics


if len(sys.argv) == 2:
    src_dir = sys.argv[1]
else:
    src_dir = './src'


# TODO FIX ENVIROMENT VARIABLES
chdir(src_dir)
chdir('..')
all_dir = './processed'
data_dir = './data/lyrics'
extract_lyrics = None

def is_alpha(letter):
    try:
        return letter.encode('ascii').isalpha()
    except:
        return False


def get_file_name(artist, track):
    artist_format = artist.lower()
    artist_format = artist_format.capitalize()
    track_format = track.lower()
    final_string = artist_format + " " + track_format
    final_string = "".join(c for c in final_string
                           if is_alpha(c) or c == " " or c == '-' or c.isnumeric())
    final_string = " ".join(final_string.split()).replace(" ", "-")
    return final_string

all_file = f"{all_dir}/all_with_latin.csv"
df = pd.read_csv(all_file, sep=';')

total = len(df[df['lyrics'].isna()].index)
print(f"Going to process {total} songs")
count = 0
found_lyrics = 0
for index, row in df[df['lyrics'].isna()].iterrows():
    # if count > 300:
    #     break
    count += 1
    artist = row['artist']
    track = row['track']
    search = f"{track} by {artist}"
    filename = get_file_name(artist, track)
    file = f"{data_dir}/{filename}.txt"
    if artist == 'Paco De Lucia':
        with open(file, 'w', encoding='utf8') as f:
            f.write('')
        df.at[index, 'lyrics'] = file
        found_lyrics += 1
        continue
    else:
        print(f"File should be {file}")

print(f"Saving to file with new found paths: {found_lyrics}")
df.to_csv(all_file, sep=';', mode="w", index=False, encoding='utf8')
