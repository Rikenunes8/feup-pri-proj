import re

def normalize_lyrics(lyrics):
    #Replace [Verse n] or other annotations with ''
    lyrics  = re.sub('\[.*?\]', '', lyrics, flags=re.S)
    lyrics = lyrics.replace("\n\n", "\n")
    lyrics = lyrics.replace(";", ",") #Might give problem with separators might as well
    return lyrics