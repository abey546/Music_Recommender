# website/spotify.py
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def authenticate_spotify():
    client_id = "d4adab7e201b4947b62eac1fdb936703"
    client_secret = "055e5d4780d04dc595ab2259c7d1fb83"
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp

def get_song_recommendations(song_title):
    sp = authenticate_spotify()
    
    # Search for the song on Spotify
    results = sp.search(q=song_title, limit=1)
    if not results['tracks']['items']:
        return []

    song = results['tracks']['items'][0]
    song_id = song['id']

    # Get recommendations based on the song
    recommendations = sp.recommendations(seed_tracks=[song_id], limit=5)

    recommended_songs = []
    for track in recommendations['tracks']:
        recommended_songs.append({
            'title': track['name'],
            'artist': track['artists'][0]['name']
        })
    
    return recommended_songs

