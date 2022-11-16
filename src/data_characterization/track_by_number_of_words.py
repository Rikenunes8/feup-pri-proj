from sys import argv
import pandas as pd
import numpy as np
import os
import re
import matplotlib.pyplot as plt


if len(argv) == 2:
    lyrics_dir = argv[1]
else:
    lyrics_dir = './data/lyrics'

lyric_files = os.listdir(lyrics_dir)
song_lyrics = {}
text = ""
i = 0
for filename in lyric_files:
    with open(os.path.join(lyrics_dir, filename), 'r', encoding='utf-8') as f:
        file_lyrics = f.read()
    normal_file_lyrics = re.sub('\[.*?\]', '', file_lyrics, flags=re.S)
    song_lyrics[filename] = normal_file_lyrics
    i += 1

data = []
data_len = []
for i, lyrics in song_lyrics.items():
    s = re.sub("\s+", " ", lyrics)
    words = s.split(' ')
    data.append(words)
    data_len.append(len(words))

data_len_log = np.log10(data_len)

plt.hist(data_len, range(0, 1500, 50))
plt.title('Track length by number of words')
plt.xlabel("# of words in a track")
plt.ylabel('# of tracks')
plt.savefig('analysis/track_by_number_of_words.svg')

plt.figure()
plt.hist(data_len_log, bins=20)
plt.title('Track length by number of words (log)')
plt.xlabel("log10(# of words) in a track")
plt.ylabel('# of tracks')
plt.savefig('analysis/track_by_number_of_words_log.svg')

plt.figure()
plt.boxplot(data_len, showfliers= True)
plt.title('Track length by number of words (boxplot)')
plt.xticks([1], ['tracks'])
plt.ylabel('# of words in a track')
plt.savefig('analysis/track_by_number_of_words_box.svg')

plt.figure()
plt.boxplot(data_len, showfliers= True)
plt.title('Track length by number of words (boxplot)')
plt.xticks([1], ['tracks'])
plt.yscale('log')
plt.ylabel('log10(# of words) of words in a track')
plt.savefig('analysis/track_by_number_of_words_box_log.svg')

