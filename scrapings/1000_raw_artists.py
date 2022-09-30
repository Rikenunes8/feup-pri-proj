# https://chartmasters.org/most-streamed-artists-ever-on-spotify/
# 23/09/2022
with open("1000_raw_artists.txt", "r", encoding='utf8') as f:
    data = f.readlines()

names = [record.split("\t")[1] for record in data]
print(names)
with open("1000_artists.txt", "w") as f:
    f.write('\n'.join(names))