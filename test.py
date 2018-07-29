import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Make your own Spotify app at https://beta.developer.spotify.com/dashboard/applications
client_id = 'f9e7bf70628e48acb0ae0878c7e28189'
client_secret = '6dbea35c563749039101f428b08a8437'
uri = "spotify:track"
      #'spotify:track:0BCPKOYdS2jbQ8iyB56Zns'


client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False
features = sp.artists(uri)
print(features)
print(uri)
print('done')