import requests
from bs4 import BeautifulSoup

def artist_top_tracks(artist_name, n):
    n = 50 if n > 50 else n

    url = "https://www.top50songs.info/artist.php"
    q = {'artist': artist_name}
    
    data = requests.get(url, q).content

    soup = BeautifulSoup(data, 'html.parser')
    res1 = soup.find('div', {'class': 'div1_left'}).findChild('ul').findAll('li')
    res2 = soup.find('div', {'cl***': 'div1_right'}).findChild('ul').findAll('li')
    first25tracks = [track.findChild('a')['title'] for track in res1]
    last25tracks = [track.findChild('a')['title'] for track in res2]
    top50tracks = first25tracks + last25tracks
    return top50tracks[:n]


with open("1000_artists.txt", "r", encoding='utf8') as f:
    artists = f.readlines()
    
artists = list(map(lambda x: x.strip(), artists))
artistTracks = {}
for artist in artists[:10]:
    top = artist_top_tracks(artist, 10)
    artistTracks[artist] = top

for key in artistTracks.keys():
    for track in artistTracks[key]:
        print(key + "\t" + track)