from bs4 import BeautifulSoup
from bs4.element import Comment
import requests
import re

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
        if is_alpha(c) or c == " ")
    
    return 'https://genius.com/' + final_string.replace(" ", "-") + "-lyrics"



def get_lyrics(artist, song):
    url = get_url(artist, song)
    html = requests.get(url).content
    outter_soup = BeautifulSoup(html, 'html.parser')
    outter_html = outter_soup.find_all('div', {'data-lyrics-container': 'true'})
    out = ""
    for i in outter_html:
        inner_html = str(i)
        internal_soup = BeautifulSoup(inner_html, 'html.parser')
        intetnal_texts = internal_soup.find_all(text=True)
        visible_texts = list(filter(is_visible, intetnal_texts))

        out += "\n".join(visible_texts)
    if out == "":
        raise Exception("not known")
    return out

print(get_lyrics("demondice", "DEMONDICEは"))