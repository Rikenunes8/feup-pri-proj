from sys import argv
import pandas as pd
import os
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt


if len(argv) == 2:
    lyrics_dir = argv[1]
else:
    lyrics_dir = './data/lyrics'

lyric_files = os.listdir(lyrics_dir)
bad_text = ""
text = ""
i = 0
for filename in lyric_files:
    with open(os.path.join(lyrics_dir, filename), 'r', encoding='utf-8') as f:
        file_lyrics = f.read()
    normal_file_lyrics = re.sub('\[.*?\]', '', file_lyrics, flags=re.S)
    text += normal_file_lyrics
    i += 1

wordcloud = WordCloud().generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
wordcloud.to_file("analysis/wordcloud.png")

