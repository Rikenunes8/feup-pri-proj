from bs4 import BeautifulSoup
# https://www.thefamouspeople.com/musicians.php
with open("./musicians.html" , "r", encoding='utf8') as f:
    data = f.read()

soup = BeautifulSoup(data, 'html.parser')
mydivs = soup.find_all("a", {"class": "tileLink"})
artists = [div.string for div in mydivs if div.string is not None]
print(artists)
with open('artists.txt', 'w') as f:
    f.write('\n'.join(artists))