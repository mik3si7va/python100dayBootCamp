import re
from datetime import datetime

# date = input(
#     "which year do you want to travel to? type the date in YYYY-MM-DD format:\n>>> "
# )

date = "2026-04-18"

if re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", date) is None:
    print("Invalid date format. Please use YYYY-MM-DD.")
    raise SystemExit(1)

try:
    datetime.strptime(date, "%Y-%m-%d")
except ValueError:
    print("Invalid date. Please enter a real date in YYYY-MM-DD format.")
    raise SystemExit(1)


import requests
from bs4 import BeautifulSoup

response = requests.get(f"https://appbrewery.github.io/bakeboard-hot-100/{date}/")

if response.status_code != 200:
    print(f"Failed to retrieve data for {date}. Please check the date and try again.")
    raise SystemExit(1)

# print(f"Successfully retrieved data for {date}.")

soup = BeautifulSoup(response.text, "html.parser")

title_info = soup.select(selector=".chart-entry__info > h3")
artist_info = soup.select(selector=".chart-entry__info > span")

# print(f"title_info: {title_info[0].getText()}\nartist_info: {artist_info[0].getText()}")

list_of_songs = []

for title, artist in zip(title_info, artist_info):
    list_of_songs.append([title.getText(), artist.getText()])

# for n in range(3):
#     print(f'{n + 1}. "{list_of_songs[n][0]}" by {list_of_songs[n][1]}')

from ytmusicapi import YTMusic
from pathlib import Path

yt = YTMusic(str(Path(__file__).with_name("browser.json")))

playlists = yt.get_library_playlists()
print(f"found {len(playlists)} playlists in your library.")

for playlist in playlists:
    if playlist["title"] == f"Billboard Hot 100 - {date}":
        print(f"playlist already exists: {playlist['title']}")
        print(
            f"playlist url: https://music.youtube.com/playlist?list={playlist['playlistId']}"
        )
        raise SystemExit(0)

playlist_id = yt.create_playlist(
    title=f"Billboard Hot 100 - {date}",
    description=f"Top 100 songs from Billboard Hot 100 on {date}.",
    privacy_status="PRIVATE",
)

if not isinstance(playlist_id, str):
    raise RuntimeError(f"Failed to create playlist: {playlist_id}")

for n, song in enumerate(list_of_songs):
    search_results = yt.search(f"{song[0]} {song[1]}", filter="songs")
    if not search_results:
        print(f"Song not found: {song[0]} by {song[1]}")
        continue

    video_id = search_results[0]["videoId"]
    yt.add_playlist_items(playlistId=playlist_id, videoIds=[video_id])
    print(f'Added "{song[0]}" by {song[1]} to the playlist.')

print(f"playlist url: https://music.youtube.com/playlist?list={playlist['playlistId']}")
