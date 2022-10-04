from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

load_dotenv()

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)


data = pd.read_csv('rolling_stones.csv')
print(data)

all_albums_tracks = []
albums_ids = []
for index, row in data.iterrows():
    result = sp.search(row['album'] + ' ' + row['artist'], limit=1, type='album')
    album = result['albums']['items'][0]['uri']
    albums_ids.append(album)
    result = sp.album_tracks(album)
    album_items = result['items']
    albums_tracks = [[item['name'], row['album'], row['artist']] for item in album_items]
    all_albums_tracks.extend(albums_tracks)

tracks = pd.DataFrame(all_albums_tracks, columns=['track', 'album', 'artist'])
print(tracks)
tracks.to_csv('rolling_stones_tracks.csv', index=False, mode='w', encoding='utf8')

