import requests
import spotipy
from spotipy import SpotifyClientCredentials
import json
from secrets import my_id, client_id, client_secret

credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spot = spotipy.Spotify(client_credentials_manager=credentials)


class PlaylistCreator:

    def __init__(self):
        self.my_id = my_id
        self.mapping = {}

    def get_playlists(self, user_id):
        playlists = spot.user_playlists(user=user_id)["items"]

        for playlist in playlists:
            self.parse_playlist(playlist)

        for key in self.mapping.keys():
            print(f"Playlist {key}: acoustic ({self.mapping[key][0]}) dance ({self.mapping[key][1]})")

    def parse_playlist(self, playlist):
        playlist_name = playlist["name"]
        spotify_id = playlist["id"]
        # Returns a list of tracks
        tracks = spot.playlist_tracks(spotify_id)["items"]

        acoustic_score = 0
        dance_score = 0

        for track in tracks:
            track_object = track["track"]
            track_name = track_object["name"]
            track_id = track_object["id"]
            features = spot.audio_features(tracks=[track_id])[0]
            acoustic_score += round(features["acousticness"], 2)
            dance_score += round(features["danceability"], 2)

        scores = [acoustic_score, dance_score]
        self.mapping[playlist_name] = scores


scraper = PlaylistCreator()
scraper.get_playlists("sourabhm3")



