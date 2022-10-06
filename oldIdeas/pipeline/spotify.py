import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import base64

load_dotenv()

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)


with open("./spotify.txt", "r") as f:
    data = f.readlines()


spotify_playlists_tracks = [
    sp.playlist_tracks(p_id) for p_id in data
]

tracks = []
for playlist_tracks in spotify_playlists_tracks:
    tracks.extend(playlist_tracks['items'])

def info_from_track(track):
    name = track['track']['name']
    if 'isrc' in track['track']['external_ids']:
        isrc = track['track']['external_ids']['isrc']
    else:
        isrc = ''
    
    album = track['track']['album']['name']
    artists = [artist['name'] for artist in track['track']['artists']]
    return {
        'name': name,
        'album': album,
        'artists': artists,
        'isrc': isrc
    }

data_tracks = []
data_albums = set()
data_artists = set()
count = 0
for track in tracks:
    count+=1
    info = info_from_track(track)
    data_tracks.append(info)
    data_albums.add(info['album'])
    data_artists.update(info['artists'])

with open("tracks.txt", "w", encoding='utf8') as f:
    f.write("name,isrc,album,artists\n")
    f.writelines(
        '\n'.join(list(map(
            lambda track: f"{track['name']},{track['isrc']},{track['album']},{';'.join(track['artists'])}"
        , data_tracks)))
    )


with open("artists.txt", "w", encoding='utf8') as f:
    f.writelines('\n'.join((list(data_artists))))

with open("albums.txt", "w", encoding='utf8') as f:
    f.writelines('\n'.join(list(data_albums)))
