import json
from pprint import pprint

with open('billboard[3000:3041].json') as f:
    data = json.load(f)

artist_list = []
song_list = []



songlist = []
x = 0
j = 1
# while x < 42: this is the total amount of files
while x < 4:
    while j < 10:
        art = data[x]['0'][j]['Artist']
        song = data[x]['0'][j]['Song']
        print(song + ':    ' + art)
        songlist.append(song + '  ' + art)
        j += 1
    x += 1
    j = 0
