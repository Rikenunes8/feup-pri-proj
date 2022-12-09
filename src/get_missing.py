import pandas as pd
import sys
from lyrics_extractor import SongLyrics
from os import getenv, chdir
from dotenv import load_dotenv
from utils import normalize_lyrics


if len(sys.argv) == 2:
    src_dir = sys.argv[1]
else:
    src_dir = './src'


# TODO FIX ENVIROMENT VARIABLES
chdir(src_dir)
load_dotenv()
chdir('..')
API_KEY = getenv('SEARCH_ENGINE_KEY')
ENGINE_ID = getenv('SEARCH_ENGINE_ID')
all_dir = './processed'
data_dir = './data/lyrics'

extract_lyrics = SongLyrics(API_KEY, ENGINE_ID)


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


all_file = f"{all_dir}/all.csv"
df = pd.read_csv(all_file, sep=';')

total = len(df[df['lyrics'].isna()].index)
print(f"Going to process {total} songs")
count = 0
for index, row in df[df['lyrics'].isna()].iterrows():
    count += 1
    artist = row['artist']
    track = row['track']
    search = f"{track} by {artist}"
    try:
        lyrics = extract_lyrics.get_lyrics(search)
        # lyrics = {'lyrics': 'No lyrics found'}
        if lyrics is not None:
            if not 'lyrics' in lyrics:
                continue
            lyrics = lyrics['lyrics']
            lyrics = normalize_lyrics(lyrics)
            filename = get_file_name(artist, track)
            file = f"{data_dir}/{filename}.txt"
            df.at[index, 'lyrics'] = file
            with open(file, 'w', encoding='utf-8') as f:
                f.write(lyrics)
            print(f"Processed  {count}/{total} and found lyrics for {search}.")

        else:
            print(f"Processed  {count}/{total} but found no lyrics for {search}")

    except Exception as e:
        if e.args[0] == {'error': 'No results found'}:
            print(f"Processed  {count}/{total} but found no lyrics for {search}")
            continue
        else:
            print(f"Unexpected error: {e}")
            print("Probably ran out of api calls")
            break
        print("Probably ran out of api calls")
        break

print("Saving to file with new found paths")
df.to_csv(all_file, sep=';', mode="w", encoding='utf8')
