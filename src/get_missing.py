import pandas as pd
import sys
from lyrics_extractor import SongLyrics
from os import getenv, chdir
import os
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
API_KEYS_STRING = getenv('SEARCH_ENGINE_KEY')
ENGINE_IDS_STRING = getenv('SEARCH_ENGINE_ID')
api_keys = API_KEYS_STRING.split(' ')
engine_ids = ENGINE_IDS_STRING.split(' ')
all_dir = './processed'
data_dir = './data/lyrics'
extract_lyrics = None

def get_extract_lyrics():
    if len(api_keys) == 0 or len(engine_ids) == 0:
        return False
    API_KEY = api_keys.pop(0)
    ENGINE_ID = engine_ids.pop(0)
    global extract_lyrics
    extract_lyrics = SongLyrics(API_KEY, ENGINE_ID)
    return True

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


get_extract_lyrics()
all_file = f"{all_dir}/all_with_latin.csv"
df = pd.read_csv(all_file, sep=';')

total = len(df[df['lyrics'].isna()].index)
print(f"Going to process {total} songs")
count = 0
has_new_key = True
for index, row in df[df['lyrics'].isna()].iterrows():
    if not has_new_key:
        break
    count += 1
    artist = row['artist']
    track = row['track']
    search = f"{track} by {artist}"
    filename = get_file_name(artist, track)
    file = f"{data_dir}/{filename}.txt"
    if os.path.isfile(file):
        df.at[index, 'lyrics'] = file
        print("File already exists. Skipping")
        continue


    while True:
        try:
            lyrics = extract_lyrics.get_lyrics(search)
            # lyrics = {'lyrics': 'No lyrics found'} 

        except Exception as e:
            if e.args[0] == {'error': 'No results found'}:
                print(f"Processed  {count}/{total} but found no lyrics for {search}")
                break
            else:
                print(f"Unexpected error: {e}")
                print("Probably ran out of api calls")
                has_new_key = get_extract_lyrics()
                if not has_new_key:
                    print("No more api keys")
                    break
                continue

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
            break

        else:
            print(f"Processed  {count}/{total} but found no lyrics for {search}")

print("Saving to file with new found paths")
df.to_csv(all_file, sep=';', mode="w", index=False, encoding='utf8')
