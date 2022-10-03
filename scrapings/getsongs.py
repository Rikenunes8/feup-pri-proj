# import requests
# from bs4 import BeautifulSoup

# def artist_top_tracks():

#     url = "https://genius.com/The-beatles-yesterday-lyrics"
    
#     data = requests.get(url).content
#     soup = BeautifulSoup(data, 'html.parser')
#     # div_lyrics = soup.find_all("span", {"class": "ReferentFragmentdesktop__Highlight-sc-110r0d9-1 jAzSMw"})
#     div_lyrics = soup.find_all(text=True)
#     for i in div_lyrics:
#         print(i)
#         print()

#     # print(div_lyrics)
#     # (class = 'Lyrics__Container-sc-1ynbvzw-6 YYrds'))
    

    

# artist_top_tracks()
#     # soup = BeautifulSoup(data, 'html.parser')
#     # res1 = soup.find('div', {'class': 'div1_left'}).findChild('ul').findAll('li')
#     # res2 = soup.find('div', {'cl***': 'div1_right'}).findChild('ul').findAll('li')
#     # first25tracks = [track.findChild('a')['title'] for track in res1]
#     # last25tracks = [track.findChild('a')['title'] for track in res2]
#     # top50tracks = first25tracks + last25tracks
#     # return top50tracks[:n]


# # with open("1000_artists.txt", "r", encoding='utf8') as f:
# #     artists = f.readlines()
    
# # artists = list(map(lambda x: x.strip(), artists))
# # artistTracks = {}
# # for artist in artists[:10]:
# #     top = artist_top_tracks(artist, 10)
# #     artistTracks[artist] = top

# # for key in artistTracks.keys():
# #     for track in artistTracks[key]:
# #         print(key + "\t" + track)

from bs4 import BeautifulSoup
from bs4.element import Comment
import requests


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.find_all(text=True)
    visible_texts = list(filter(tag_visible, texts))
    first = -1
    last = -1
    
    for i in range(0, len(visible_texts)):
        if 'Lyrics' in visible_texts[i] and first == -1:
            first = i+1
        if 'You might also like' in visible_texts[i]:
            last = i 
    print(first)
    print(last)
    return visible_texts[first: last]

html = requests.get('https://genius.com/The-beatles-yesterday-lyrics').content
print(text_from_html(html))