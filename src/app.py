import spotipy
import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import matplotlib.pyplot as plt


load_dotenv()




CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

spotipy.Spotify()

artist_id = "7HGNYPmbDrMkylWqeFCOIQ"

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

top_tracks = sp.artist_top_tracks(artist_id)
print(top_tracks)

for track in top_tracks['tracks'][:10]:
    print(track['name'])
    print(track['popularity'])
    print(track['duration_ms'])

import pandas as pd

# Your dictionary
data = {
    'tracks': [
        # ... (your track data)
    ]
}

# Extracting track name, popularity, and duration
track_data = []
for track in top_tracks['tracks'][:10]:
    name = track['name']
    popularity = track['popularity']
    duration_ms = track['duration_ms']
    track_data.append({'name': name, 'popularity': popularity, 'duration_ms': duration_ms})

# Creating DataFrame
df = pd.DataFrame(track_data)

# Displaying the DataFrame
print(df)



plt.figure(figsize=(10, 6))
plt.scatter(df["duration_ms"], df["popularity"], c=df.index, cmap="Set1")
plt.title("Relationship Between Song Duration and Popularity")
plt.xlabel("Duration (milliseconds)")
plt.ylabel("Popularity")
plt.colorbar(label="Track Index")

plt.tight_layout()
plt.savefig("scatterplot.png")
plt.show()

print("After taking a look at the scatterplot, I see no relation between duration and popularity.")
