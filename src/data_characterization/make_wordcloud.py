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
print(f"Number of files {len(lyric_files)}")
for filename in lyric_files:
    with open(os.path.join(lyrics_dir, filename), 'r', encoding='utf-8') as f:
        file_lyrics = f.read()
    # normal_file_lyrics = re.sub('\[.*?\]', '', file_lyrics)
    normal_file_lyrics = re.sub('\[.*?\]', '', file_lyrics, flags=re.S)
    # normal_file_lyrics = re.sub('\n{2}','',lyrics)  # Remove gaps between verses
    # normal_file_lyrics = str(lyrics).strip('\n')
    text += normal_file_lyrics
    i += 1
    print(f"{i}")


wordcloud = WordCloud().generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

wordcloud.to_file("analysis/wordcloud.png")

