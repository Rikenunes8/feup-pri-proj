from sys import argv
import os
import re
import json
import spacy
from spacy.language import Language
from spacy_langdetect import LanguageDetector

def get_lang_detector(nlp, name):
    return LanguageDetector()

if len(argv) == 2:
    lyrics_dir = argv[1]
else:
    lyrics_dir = '../../data/lyrics'


def map_spacy_solr(lang):
    mapping = {
        'en': 'en',
        'es': 'es',
        'fr': 'fr',
        'de': 'de',
        'it': 'it',
        'pt': 'pt',
        'nl': 'nl'
    }
    if lang in mapping:
        return mapping[lang]
    else:
        print("language not being mapped")
        return 'en'
def get_lang(lyrics):
    try:
        nlp = spacy.load("en_core_web_sm")
        nlp = spacy.load("xx_ent_wiki_sm")
        Language.factory("language_detector", func=get_lang_detector)
        nlp.add_pipe('sentencizer')
        nlp.add_pipe('language_detector', last=True)
        doc = nlp(lyrics)

        return doc._.language
    except:
        print("Missing libraries, please install spacy and spacy_langdetect")
        print("pip install spacy_langdetect")
        print("python -m spacy download en_core_web_sm")
        print("python -m spacy download en_core_web_lg [Optional?]")
        print("python -m spacy download xx_ent_wiki_sm")

    
get_lang("Isto é um teste")	

first = True
counter = 0
with open('../data/tracks.json', 'w', encoding='utf-8') as jf:
    jf.write('[\n')
    with open('../../processed/all.csv', 'r', encoding='utf-8') as f:
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
                spacy_lang = get_lang(track_lyrics)
                solr_lang = map_spacy_solr(spacy_lang)
            except:
                track_lyrics=""
                solr_lang = 'en'

            track_obj = {
                "id": counter,
                "artist": artist,
                "album": album,
                "album_release_date": album_release_date,
                "album_ranking": album_ranking,
                "n_tracks": n_tracks,
                "track": track,
                "track_duration": track_duration,
                "lyrics": track_lyrics,
                "language": solr_lang
            }
            print(track_obj)
            if not first:
                jf.write(',\n')

            jf.write(json.dumps(track_obj, indent=4))

            first = False
            counter += 1
    jf.write(']\n')
    

