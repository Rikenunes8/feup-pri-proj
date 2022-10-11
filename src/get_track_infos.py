from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import sys
import os
import json
from Levenshtein import distance


def get_closest_album(album_items, album_name, artist_name):
    artists_lists = [album['artists'] for album in album_items]
    artists_names_distances = [[distance(artist_name, album_artist['name'], processor=lambda x: x.lower()) for album_artist in album_artists_list] for album_artists_list in artists_lists]
    min_artists_names_distances = [min(album_artist_list) for album_artist_list in artists_names_distances]

    relevant_albums = []
    for i, val in enumerate(min_artists_names_distances):
        if val <= 5:
            relevant_albums.append(album_items[i])
    # if min_artist_name > 5:
    #     return None
    if len(relevant_albums) == 0:
        relevant_albums = album_items
        
    album_items_names = [album['name'] for album in relevant_albums]
    album_items_distance_names = [distance(album_name, item_name, weights=(
        3, 1, 3), processor=lambda x: x.lower()) for item_name in album_items_names]
    closest_album = album_items[album_items_distance_names.index(
        min(album_items_distance_names))]
    return closest_album


def get_tracks(album_uri):
    result = []
    page = 0
    while True:
        album_data = sp.album_tracks(album_uri, limit=50, offset=page)
        album_items = album_data['items']

        result.extend(album_items)
        if len(album_items) < 50:
            break

        page += 50

    return result


load_dotenv()

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)


if len(sys.argv) < 4:
    print("Must take a filename, an album and an artist")
    exit(1)

filename = sys.argv[1]
album_name = sys.argv[2]
artist_name = sys.argv[3]
ranking = sys.argv[4]

columns = ['artist', 'album', 'album_release_date',
           'ranking', 'track', 'track_duration (s)']

result = sp.search(f"{album_name} {artist_name}", limit=10, type='album')
albums = result['albums']['items']
if len(albums) == 0:
    exit(1)
closest_album = get_closest_album(albums, album_name, artist_name)
album = closest_album['uri']
# album = albums[0]['uri']
album_items = get_tracks(album)
albums_tracks = [[artist_name, album_name, albums[0]['release_date'], ranking,
                  item['name'], round(item['duration_ms']/1000)] for item in album_items]
tracks = pd.DataFrame(albums_tracks, columns=columns)
print(tracks)

addHeader = not os.path.isfile(filename)
mode = 'w' if addHeader else 'a'
tracks.to_csv(filename, header=addHeader, index=False,
              mode=mode, encoding='utf8', sep=';')
