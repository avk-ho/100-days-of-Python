# https://www.udemy.com/course/100-days-of-code/learn/lecture/21624096#overview

# Day 46
# Musical time machine project
# Unfinished

from bs4 import BeautifulSoup
import pprint
import requests

##### Getting data from billboard

date_input = input("Which date do you want to travel to ? Type in YYYY-MM-DD format: ")
top_url = f"https://www.billboard.com/charts/hot-100/{date_input}"
# 2000-08-12

response = requests.get(url=top_url)
top_website = response.text
soup = BeautifulSoup(top_website, "html.parser")
top_songs = soup.select("h3.c-title.a-no-trucate")
top_artists = soup.select("span.c-label.a-no-trucate")
# print(top_songs)
# print(top_artists)
top_list = []
for i in range(len(top_songs)):
    new_item = {}
    song_name = top_songs[i].getText().strip()
    artist_name = top_artists[i].getText().strip()
    # print(song_name)
    # print(artist_name)
    new_item["song"] = song_name
    new_item["artist"] = artist_name
    top_list.append(new_item)

# print(top_list)

###### Setting up the app with spotify/spotipy
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = ""
SPOTIFY_SECRET_ID = ""
SPOTIFY_REDIRECT_URI = "http://example.com"

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIFY_REDIRECT_URI,
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_SECRET_ID,
        cache_path="token.txt",
        show_dialog=True
    )
)


user_id = spotify.current_user()["id"]
print(user_id)

result = spotify.search(f"track:{top_list[0]['song']} year:")
print(result)
