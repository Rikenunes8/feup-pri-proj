from sys import argv
from bs4 import BeautifulSoup
import os

if len(argv) != 3:
    raise Exception("wrong number of arguments")
filename_html = argv[1]
filename_csv = argv[2]

if os.path.isfile(filename_csv):
    print('File {} already exists'.format(filename_csv))
    exit(0)


with open(filename_html, "r", encoding='utf8') as f:
    wiki_page = f.read()

wiki = BeautifulSoup(wiki_page, 'html.parser')
table_lines = wiki.find('div', {'id':'mw-content-text'}).findChild('div', {'class':'mw-parser-output'}).findChild('table', {'class':'wikitable'}).findChild('tbody').findChildren('tr')

rolling_stones = [['album', 'artist', 'ranking']]
for line in table_lines[1:]:    
    lineChildrensTd = line.findChildren('td')
    ranking = lineChildrensTd[0].find(text=True)
    album = line.findChild('th').findChild('i').find(text=True)
    artist = lineChildrensTd[1].find(text=True)
    rolling_stones.append([album, artist, ranking])

with open(filename_csv, "w", encoding='utf8') as f:
    f.write('\n'.join('{};{};{}'.format(pair[0], pair[1], pair[2]).strip() for pair in rolling_stones))
