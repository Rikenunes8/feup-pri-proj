from sys import argv
import sys
from bs4 import BeautifulSoup
from bs4.element import Comment
import requests
import os
import unidecode

if len(argv) != 4:
    raise Exception("wrong number of arguments")

dir =  argv[1]
song = argv[2]
artist = argv[3]
filename_to_save = None

def is_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def is_alpha(letter):
    try:
        return letter.encode('ascii').isalpha()
    except:
        return False

def get_url(artist, song):
    artist_format = artist.lower()
    artist_format = artist_format.capitalize()
    song_format = song.lower()
    final_string = artist_format + " " + song_format
    final_string = "".join(c for c in final_string 
        if is_alpha(c) or c == " " or c == '-' or c.isnumeric())
    final_string = " ".join(final_string.split()).replace(" ", "-")
    global filename_to_save
    filename_to_save = final_string
    return 'https://genius.com/' + final_string + "-lyrics"



def get_lyrics(artist, song):
    artist = unidecode.unidecode(artist)
    song = unidecode.unidecode(song)

    url = get_url(artist, song)
    response = requests.get(url)
    if (response.status_code != 200):
        
        song = song.split('(')[0].split('-')[0].split(' by ')[0].strip()
        url = get_url(artist, song)
        response = requests.get(url)
        if (response.status_code != 200):
            with open('data/log.txt', 'a', encoding='utf-8') as f:
                f.write(artist + ";" + song + "; lyrics not found\n")
            exit(1)
    # print(url)
    
    html = response.content
    outter_soup = BeautifulSoup(html, 'html.parser')
    outter_html = outter_soup.find_all('div', {'data-lyrics-container': 'true'})
    out = ""
    for internal_soup in outter_html:
        internal_texts = internal_soup.find_all(text=True)
        visible_texts = list(filter(is_visible, internal_texts))
        out += "\n".join(visible_texts)

    return out

directory = dir + 'lyrics'
lyrics = get_lyrics(artist, song)

path = dir + 'lyrics/' + filename_to_save + ".txt"
with open(path, 'w', encoding='utf-8') as f:
    f.write(lyrics)

sys.exit(path)

# print(get_lyrics("Britney Spears", "...Baby One More Time"))
# print(get_lyrics("Yui Ninomiya", "Dark seeks light"))
# print(get_lyrics("Lukas Graham", "7 years"))
# print(get_lyrics("chase atlantic", "23"))
# print(get_lyrics("Whitaker", "5,000,000,000 Years"))
# print(get_lyrics("shakira", "Hips Don't Lie"))
# print(get_lyrics("Modjo", "Lady - Hear Me Tonight"))




