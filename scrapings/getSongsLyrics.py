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
        if is_alpha(c) or c == " " or c.isnumeric())
    final_string = " ".join(final_string.split())
    return 'https://genius.com/' + final_string.replace(" ", "-") + "-lyrics"



def get_lyrics(artist, song):
    url = get_url(artist, song)
    print(url)
    html = requests.get(url).content
    outter_soup = BeautifulSoup(html, 'html.parser')
    outter_html = outter_soup.find_all('div', {'data-lyrics-container': 'true'})
    out = ""
    for internal_soup in outter_html:
        internal_texts = internal_soup.find_all(text=True)
        visible_texts = list(filter(is_visible, internal_texts))

        out += "\n".join(visible_texts)
    if out == "":
        raise Exception("not known")
    return out

# print(get_lyrics("Britney Spears", "...Baby One More Time"))
# print(get_lyrics("Yui Ninomiya", "Dark seeks light"))
# print(get_lyrics("Lukas Graham", "7 years"))
# print(get_lyrics("chase atlantic", "23"))
# print(get_lyrics("Whitaker", "5,000,000,000 Years"))
# print(get_lyrics("shakira", "Hips Don't Lie"))
print(get_lyrics("Modjo", "Lady - Hear Me Tonight"))
