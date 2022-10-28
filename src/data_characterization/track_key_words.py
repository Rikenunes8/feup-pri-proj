from sys import argv
import pandas as pd
import numpy as np
import os
import re
import matplotlib.pyplot as plt
from keybert import KeyBERT
from wordcloud import WordCloud
from collections import Counter


if len(argv) == 2:
    lyrics_dir = argv[1]
else:
    lyrics_dir = './data/lyrics'

lyric_files = os.listdir(lyrics_dir)
song_lyrics = {}
text = ""
i = 0
print(f"Number of files {len(lyric_files)}")
for filename in lyric_files:
    with open(os.path.join(lyrics_dir, filename), 'r', encoding='utf-8') as f:
        file_lyrics = f.read()
    # normal_file_lyrics = re.sub('\[.*?\]', '', file_lyrics)
    normal_file_lyrics = re.sub('\[.*?\]', '', file_lyrics, flags=re.S)
    # normal_file_lyrics = re.sub('\n{2}','',lyrics)  # Remove gaps between verses
    # normal_file_lyrics = str(lyrics).strip('\n')
    song_lyrics[filename] = normal_file_lyrics
    i += 1
    print(f"{i}")

    if i == 20:
        break


kw_model = KeyBERT(model='all-mpnet-base-v2')

data_all_keywords = []

print(f"Total lyrics {len(song_lyrics)}")
count = 0
for i, lyrics in song_lyrics.items():

    lyrics = re.sub("\s+", " ", lyrics)
    keywords = kw_model.extract_keywords(lyrics, 

                                     keyphrase_ngram_range=(1, 3), 

                                    #  stop_words='english', 

                                     highlight=False,

                                     top_n=3)

    keywords_list= list(dict(keywords).keys())
    data_all_keywords.extend(keywords_list)
    count+=1
    print(count)
    
word_cloud_lst = Counter(data_all_keywords)
wordcloud = WordCloud().generate_from_frequencies(word_cloud_lst)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

wordcloud.to_file("analysis/all_keywords_wordcloud.png")
