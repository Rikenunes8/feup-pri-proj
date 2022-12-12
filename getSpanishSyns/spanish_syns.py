import requests
from bs4 import BeautifulSoup
from unidecode import unidecode

url = 'https://www.wordreference.com/sinonimos/'

fw = open('synonyms_es.txt', 'a')

with open('Spanish_.txt', 'r', encoding='utf-8') as f:
    while True:
        word_original = f.readline()
        if not word_original:
            break
        word_strip = word_original.split('/')[0].strip().lower()
        word = unidecode(word_strip)
        print(word)

        search = url + word
        try:
            resp = requests.get(search)
            soup=BeautifulSoup(resp.text, features="lxml")
            
            l = soup.find(class_='trans clickable')
            syn = l.find('li')
            toWrite = word_strip + ', ' + syn.next_element
            fw.write(toWrite + '\n')
        except:
            print('Not found')
        
f.close()
