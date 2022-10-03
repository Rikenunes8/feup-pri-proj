import requests
import os
import json
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

base_url = "https://api.musixmatch.com/ws/1.1/"

def save_to_csv(d, file, append):
    mode = 'w' if not append else 'a'
    df = pd.DataFrame.from_dict(d)
    df.to_csv('data/'+file, index=False, mode=mode)
def load_csv(file):
    return pd.read_csv('data/'+file)


def print_json(json_data):
    json_formatted_str = json.dumps(json_data, indent=2)
    print(json_formatted_str)

def get_from_json(json, path):
    for x in path:
        if ((type(x) == str and x not in json) or (type(x) == int and x >= len(json))):
            return None
        else:
            json = json[x]
    return json


def get_artist(apikey, artist_name):
    method = 'artist.search'
    url = base_url + method
    q = {'apikey': apikey, 'q_artist': artist_name, 'page_size': 5}

    data = requests.get(url, q)

    status = data.status_code
    if status == 200:
        json_data = data.json()
        artists_json = get_from_json(json_data, ['message','body','artist_list'])
        artist_id = get_from_json(artists_json, [0,'artist','artist_id'])
        artist_name = get_from_json(artists_json, [0,'artist','artist_name'])
        return (artist_id, artist_name)
    else:
        pass

def get_artist_albums(apikey, artist_id, sort_by_release, page_size):
    method = 'artist.albums.get'
    url = base_url + method
    q = {'apikey': apikey, 'artist_id': artist_id, 's_release_date': sort_by_release, 'page_size': page_size}

    data = requests.get(url, q)

    status = data.status_code
    if status == 200:
        json_data = data.json()
        albums_json = json_data['message']['body']['album_list']
        albums = []
        for album in albums_json:
            album_id = get_from_json(album, ['album', 'album_id'])
            album_name = get_from_json(album, ['album', 'album_name'])
            album_release_date = get_from_json(album, ['album', 'album_release_date'])
            # album_track_count = get_from_json(album, ['album', 'album_track_count'])
            # album_release_type = get_from_json(album, ['album', 'album_release_type'])
            albums.append((album_id, album_name, album_release_date))
        return albums
    else:
        pass

def get_album_tracks(apikey, album_id):
    method = 'album.tracks.get'
    url = base_url + method
    q = {'apikey': apikey, 'album_id': album_id, 'f_has_lyrics': 1, 'page_size': 20}

    data = requests.get(url, q)

    status = data.status_code
    if status == 200:
        json_data = data.json()
        tracks_json = get_from_json(json_data, ['message','body','track_list'])
        tracks = []
        for track in tracks_json:
            print_json(track)
            track_id = get_from_json(track, ['track', 'track_id'])
            track_name = get_from_json(track, ['track', 'track_name'])
            tracks.append((track_id, track_name))
        return tracks
    else:
        pass



def get_scraping_names():
    with open("scrapings/1000_artists.txt", "r", encoding='utf8') as f:
        artists = f.readlines()
        
    artists = list(map(lambda x: x.strip(), artists))
    return artists

def build_artists(artists_names, artists_df:pd.DataFrame):
    artists_d = {}
    if artists_df == None:
        artists_d['artist_id'] = []
        artists_d['artist_name'] = []
    else:
        artists_d = artists_df.to_dict('list')

    for a in artists_names:
        (artist_id, artist_name) = get_artist(os.getenv('MUISXMATCH_KEY'), a)
        artists_d['artist_id'].append(artist_id)
        artists_d['artist_name'].append(artist_name)
    save_to_csv(artists_d, 'artists.csv', False)

def build_albums(artists, albums_df:pd.DataFrame):
    albums_d = {}
    if albums_df == None:
        albums_d['artist_id'] = []
        albums_d['album_id'] = []
        albums_d['album_name'] = []
        albums_d['album_release'] = []
    else:
        albums_d = albums_df.to_dict('list')

    for artist_id in artists:
        albums = get_artist_albums(os.getenv('MUISXMATCH_KEY'), artist_id, 'desc', 10)
        for (album_id, album_name, album_release) in albums:
            albums_d['artist_id'].append(artist_id)
            albums_d['album_id'].append(album_id)
            albums_d['album_name'].append(album_name)
            albums_d['album_release'].append(album_release)
    save_to_csv(albums_d, 'albums.csv', False)

def build_tracks(albums, tracks_df:pd.DataFrame):
    tracks_d = {}
    if tracks_df == None:
        tracks_d['album_id'] = []
        tracks_d['track_id'] = []
        tracks_d['track_name'] = []
    else:
        tracks_d = tracks_df.to_dict('list')

    for album_id in albums:
        tracks = get_album_tracks(os.getenv('MUISXMATCH_KEY'), album_id)
        for (track_id, track_name) in tracks:
            tracks_d['album_id'].append(album_id)
            tracks_d['track_id'].append(track_id)
            tracks_d['track_name'].append(track_name)
    save_to_csv(tracks_d, 'tracks.csv', False)


# artists_names = get_scraping_names()
# build_artists(artists_names[:15])

# d = load_csv('artists.csv')
# build_albums(d.to_dict('list')['artist_id'], None)

# d = load_csv('albums.csv')
# build_tracks(d.to_dict('list')['album_id'], None)