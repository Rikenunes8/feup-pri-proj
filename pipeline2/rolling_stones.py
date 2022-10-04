from sys import argv
from bs4 import BeautifulSoup
import requests

# url = 'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Albums/500'
# wiki_page = requests.get(url).content

if len(argv) != 2:
    raise Exception("wrong number of arguments")
filename = argv[1]
with open(filename, "r", encoding='utf8') as f:
    wiki_page = f.read()

wiki = BeautifulSoup(wiki_page, 'html.parser')
table_lines = wiki.find('div', {'id':'mw-content-text'}).findChild('div', {'class':'mw-parser-output'}).findChild('table', {'class':'wikitable'}).findChild('tbody').findChildren('tr')

rolling_stones = []
for line in table_lines[1:]:    
    album = line.findChild('th').findChild('i').find(text=True)
    artist = line.findChildren('td')[1].find(text=True)
    rolling_stones.append([album, artist])

with open("rolling_stones.csv", "w", encoding='utf8') as f:
    f.write('\n'.join('{};{}'.format(pair[0], pair[1]).strip() for pair in rolling_stones))
