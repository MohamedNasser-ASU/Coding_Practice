import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&&term=" + sys.argv[1])
js = response.json()
songs = js["results"]
for song in songs:
    print(song["trackName"])
print(response)

