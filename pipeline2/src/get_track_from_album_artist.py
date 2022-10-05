from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import sys
import os

load_dotenv()

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)


if len(sys.argv) < 4:
    print("Must take a filename, an album and an artist")
    exit(1)

filename = sys.argv[1]
album_name = sys.argv[2]
artist_name = sys.argv[3]
columns = ['track', 'album', 'artist']

result = sp.search(f"{album_name} {artist_name}", limit=1, type='album')
album_items = result['albums']['items']
if len(album_items) == 0: exit(1)
album = album_items[0]['uri']
result = sp.album_tracks(album)
album_items = result['items']
albums_tracks = [[item['name'], album_name, artist_name] for item in album_items]
tracks = pd.DataFrame(albums_tracks, columns=columns)
print(tracks)

addHeader = not os.path.isfile(filename)
mode = 'w' if addHeader else 'a'
tracks.to_csv(filename,header=addHeader, index=False, mode=mode, encoding='utf8', sep=';')

