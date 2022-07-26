import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input(
    "Which date do you want to travel to? Type in this format YYYY-MM-DD:\n")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
songs = response.text
soup = BeautifulSoup(songs, "html.parser")
song_list = soup.find_all("h3", class_="c-title", id="title-of-a-story")
translator = str.maketrans({chr(10): '', chr(9): ''})
songs_name = [song.getText().translate(translator) for song in song_list]

no_songwriter = [song for song in songs_name if song != 'Songwriter(s):']
no_producer = [song for song in no_songwriter if song != 'Producer(s):']
no_imprint = [song for song in no_producer if song !=
              'Imprint/Promotion Label:']
no_harry = [song for song in no_imprint if song !=
            'After Harry Styles, Which Pop Artist Deserves a College Course? Vote!']
no_gains = [song for song in no_harry if song != 'Gains in Weekly Performance']
with_ads = [song for song in no_gains if song != 'Additional Awards']
final = with_ads[0:100]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://api.spotify.com/v1/",
        client_id='',
        client_secret='',
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in final:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(
    user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.user_playlist_add_tracks(
    user=user_id, playlist_id=playlist["id"], tracks=song_uris)
