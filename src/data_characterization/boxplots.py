from sys import argv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

filename = './processed/all.csv'
df = pd.read_csv(filename, sep=';')

#Song duration
plt.subplot(2, 2, 1)
df['track_duration (log_s)'] = np.log10(df['track_duration (s)'])
a = df.sort_values('track_duration (s)', ascending=False).head(10)

print(a)
plt.boxplot(df['track_duration (s)'], showfliers= True)
plt.show()
# data_by_album = df.groupby(['album', 'artist'])
# sum_data_by_album = data_by_album.aggregate('sum')
# plt.hist(sum_data_by_album['track_duration (s)'].values, 20, rwidth=0.9)
# plt.savefig('./analysis/album_distribution_by_duration.svg')