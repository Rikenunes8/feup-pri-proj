from bs4 import BeautifulSoup
from bs4.element import Comment
import requests


def is_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def get_lyrics(url_end):
    outter_soup = BeautifulSoup(url_end, 'html.parser')
    outter_html = outter_soup.find_all('div', {'data-lyrics-container': 'true'})
    out = ""
    for i in outter_html:
        inner_html = str(i)
        internal_soup = BeautifulSoup(inner_html, 'html.parser')
        intetnal_texts = internal_soup.find_all(text=True)
        visible_texts = list(filter(is_visible, intetnal_texts))

        out += "\n".join(visible_texts)
    return out

html = requests.get('https://genius.com/Queen-bohemian-rhapsody-lyrics').content
print(get_lyrics(html))