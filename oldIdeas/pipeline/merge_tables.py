import pandas as pd

def save_to_csv(d, file, append):
    mode = 'w' if not append else 'a'
    df = pd.DataFrame.from_dict(d)
    df.to_csv('data/'+file, index=False, mode=mode)
def load_csv(file):
    return pd.read_csv('data/'+file)


artists = load_csv('artists.csv')
albums = load_csv('albums.csv')
tracks = load_csv('tracks.csv')

data = pd.merge(artists, albums, left_on="artist_id", right_on="artist_id", how='inner')
data = pd.merge(data, tracks, left_on="album_id", right_on="album_id", how='inner')

save_to_csv(data, 'all_data.csv', False)
