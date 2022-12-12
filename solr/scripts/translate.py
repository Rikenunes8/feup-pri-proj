from sys import argv
import os
import re
import json
import spacy
from spacy.language import Language
from spacy_langdetect import LanguageDetector
from concurrent.futures import ThreadPoolExecutor, wait
from multiprocessing import Lock

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
        'nl': 'nl',
        'pl': 'pl',
        'so': 'so',
        'ca': 'ca',
        'id': 'id',
    }
    if lang in mapping:
        warning = ''
        if lang not in ['en', 'es']:
            warning = 'Unusual lang: ' + lang
            print(warning)
        return mapping[lang], warning
    else:
        print("language not being mapped " + lang)
        return 'en', ''

def get_lang(text):
    doc = nlp(text)
    return doc._.language

try:
    nlp = spacy.load("en_core_web_sm")
    nlp = spacy.load("xx_ent_wiki_sm")
    Language.factory("language_detector", func=get_lang_detector)
    nlp.add_pipe('sentencizer')
    nlp.add_pipe('language_detector', last=True)
except:
    print("Missing libraries, please install spacy and spacy_langdetect")
    print("pip install spacy_langdetect")
    print("python -m spacy download en_core_web_sm")
    print("python -m spacy download en_core_web_lg [Optional?]")
    print("python -m spacy download xx_ent_wiki_sm")

    
warnings = []
warning_lock = Lock()
lock = Lock()
get_lang("Isto é um teste")	

def read_and_process_file(jf, line, counter):
    line = line.strip().split(';')
    artist = line[0]
    album = line[1]
    album_release_date = line[2]
    album_ranking = line[3]
    n_tracks = line[4]
    track = line[5]
    track_duration = line[6]
    track_file = line[7]
    with lock:
        id = counter
    if track_file == '':
        solr_lang = ''
    else :
        try:

            with open('./../../' + track_file, 'r', encoding='utf-8') as tf:
                track_lyrics_from_file = tf.read()
            normal_file_lyrics = re.sub('\[.*?\]:?', '', track_lyrics_from_file, flags=re.S)
            # normal_file_lyrics = re.sub('\[.*?\]', '', file_lyrics, flags=re.S)
            track_lyrics= re.sub("\s+", " ", normal_file_lyrics).strip()
            spacy_lang = get_lang(track_lyrics)
            spacy_lang_name = spacy_lang['language'] if spacy_lang['score'] > 0.9 else 'en'
            solr_lang, warning_message = map_spacy_solr(spacy_lang_name)
            if warning_message != "":
                with warning_lock:
                        warnings.append(f"For id {id}, warning: {warning_message}")
        except Exception as e:
            print('Exception in id ' + str(id) + 'track ' + track + ' in file ' + track_file, e)
            solr_lang = 'en'

    track_obj = {
        "id": id,
        "artist": artist,
        "album": album,
        "album_release_date": album_release_date,
        "album_ranking": album_ranking,
        "n_tracks": n_tracks,
        "track": track,
        "track_duration": track_duration,
        "lyrics_es": track_lyrics if solr_lang == 'es' else '',
        "lyrics_en": track_lyrics if solr_lang != 'es' else '',
        "language": solr_lang
    }
    with lock:
        counter+=1
        # print(track_obj)
        jf.write(json.dumps(track_obj, indent=4).encode('utf-8'))
        jf.write(',\n'.encode('utf-8'))

def translate_files():
    executor = ThreadPoolExecutor(max_workers=1)
    with open('../data/tracks.json', 'wb') as jf:
        futures = []
        counter = 0
        jf.write('[\n'.encode('utf-8'))
        with open('../../processed/all.csv', 'r', encoding='utf-8') as f:
            f.readline()

            while True:
                line = f.readline()
                if not line:
                    break
                counter += 1
                future = executor.submit(read_and_process_file, jf, line, counter)
                futures.append(future)
                

        wait(futures)
        jf.seek(-2, 1)
        jf.write('\n]\n'.encode('utf-8'))
        
    with open('../data/warnings.txt', 'w') as wf:
        for w in warnings:
            wf.write(w + '\n')
        

if __name__ == '__main__':
    translate_files()

    # obj = get_lang(   "Child, don't you know I don't want to let you go Child, don't you know That I don't wanna let you I don't wanna let you I don't wanna let you I don't wanna let you I don't wanna let you I don't wanna let you I don't wanna let you I don't wanna let you I don't wanna let you I don't wanna let you Styles come and go But I'm not going to let you go Styles, they come and go But I'm not gonna let you I'm not gonna let you I'm not gonna let you I'm not gonna let you I'm not gonna let you I'm not gonna let you I'm not gonna let you I'm not gonna let you I'm not gonna let you I'm not gonna let you")
    # print(obj)