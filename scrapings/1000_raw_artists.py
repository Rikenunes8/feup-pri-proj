# https://chartmasters.org/most-streamed-artists-ever-on-spotify/
with open("1000_raw_artists.txt", "r", encoding='utf8') as f:
    data = f.readlines()

names = [record.split("\t")[1] for record in data]
print(names)
with open("1000_artists.txt", "w", encoding='utf8') as f:
    f.write('\n'.join(names))