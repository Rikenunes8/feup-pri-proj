import requests
import os
import json
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

base_url = "https://api.musixmatch.com/ws/1.1/"


def get_artist_id(artist_name, apikey):
    method = 'artist.search'
    url = base_url + method
    q = {'apikey': apikey, 'q_artist': artist_name, 'page_size': 1}

    json_data = requests.get(url, q).json()
    artist_id = json_data['message']['body']['artist_list'][0]['artist']['artist_id']
    return artist_id

artist_id = get_artist_id("Drake", os.getenv('MUISXMATCH_KEY'))


# json_formatted_str = json.dumps(json_data, indent=2)
# print(json_formatted_str)