import requests
import  sys
import json

response = requests.get("https://itunes.apple.com/search", params ={"entity": "song", "limit": 50, "term": sys.argv[1]})
#print (response.json())
#print(json.dumps(response.json(), indent = 3))

parsed_data = response.json()
for song in parsed_data["results"]:
    print(song["trackName"])

