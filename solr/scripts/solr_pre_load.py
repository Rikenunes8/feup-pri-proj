from sys import argv
import os
import re
import json


if len(argv) == 2:
    lyrics_dir = argv[1]
else:
    lyrics_dir = '../../data/lyrics'



first = True
counter = 0
with open('../data/tracks.json', 'w', encoding='utf-8') as jf:
    jf.write('[\n')
    with open('../../processed/all_with_latin.csv', 'r', encoding='utf-8') as f:
        f.readline()

        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip().split(';')
            artist = line[0]
            album = line[1]
            album_release_date = line[2]
            album_ranking = line[3]
            n_tracks = line[4]
            track = line[5]
            track_duration = line[6]
            track_file = line[7]
            try:
                with open('./../../' + track_file, 'r', encoding='utf-8') as tf:
                    track_lyrics_from_file = tf.read()
                normal_file_lyrics = re.sub('\[.*?\]:?', '', track_lyrics_from_file, flags=re.S)
                # normal_file_lyrics = re.sub('\[.*?\]', '', file_lyrics, flags=re.S)
                track_lyrics= re.sub("\s+", " ", normal_file_lyrics).strip()
            except:
                track_lyrics=""

            track_obj = {
                "id": counter,
                "artist": artist,
                "album": album,
                "album_release_date": album_release_date,
                "album_ranking": album_ranking,
                "n_tracks": n_tracks,
                "track": track,
                "track_duration": track_duration,
                "lyrics": track_lyrics
            }

            if not first:
                jf.write(',\n')

            jf.write(json.dumps(track_obj, indent=4))

            first = False
            counter += 1
    jf.write(']\n')
    

