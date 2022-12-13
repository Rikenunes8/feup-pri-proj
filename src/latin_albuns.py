from bs4 import BeautifulSoup
import requests

page1 = requests.get("https://www.listchallenges.com/billboard-the-50-greatest-latin-albums-of-the")
page2 = requests.get("https://www.listchallenges.com/billboard-the-50-greatest-latin-albums-of-the/list/2")

pages = [page1, page2]

total = ""
r = 1
for page in pages:
    latin_page = BeautifulSoup(page.content, 'html.parser')
    for i in latin_page.find_all("div", {"class": "item-name"}):
        name = i.get_text().replace('\r', '')
        name = name.replace('\n', '')
        name = name.replace('\t', '')
        name = name.split('- ')
        if len(name) != 2:
            name.insert(0, name[0])
        if name[0][-1] == ' ':
            name[0] = name[0][:-1]
        name = name[1] + ";" + name[0] + ";" + str(r) +'\n'
        r+=1
        total = total + name

text= "album;artist;ranking\n" + total[:-1]

path ="./data/latin.csv"
with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
