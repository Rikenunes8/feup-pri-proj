from sys import argv
from bs4 import BeautifulSoup

# import requests
# url = 'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Albums/500'
# wiki_page = requests.get(url).content

print(argv)

if len(argv) != 3:
    raise Exception("wrong number of arguments")
filename_html = argv[1]
filename_csv = argv[2]
with open(filename_html, "r", encoding='utf8') as f:
    wiki_page = f.read()

wiki = BeautifulSoup(wiki_page, 'html.parser')
table_lines = wiki.find('div', {'id':'mw-content-text'}).findChild('div', {'class':'mw-parser-output'}).findChild('table', {'class':'wikitable'}).findChild('tbody').findChildren('tr')

rolling_stones = [['album', 'artist']]
for line in table_lines[1:]:    
    album = line.findChild('th').findChild('i').find(text=True)
    artist = line.findChildren('td')[1].find(text=True)
    rolling_stones.append([album, artist])

with open(filename_csv, "w", encoding='utf8') as f:
    f.write('\n'.join('{};{}'.format(pair[0], pair[1]).strip() for pair in rolling_stones))
