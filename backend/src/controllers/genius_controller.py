import lyricsgenius
import spotipy
from flask import Blueprint, request, jsonify, current_app
from spotipy.oauth2 import SpotifyClientCredentials

genius = Blueprint('genius', __name__, url_prefix='/genius')


@genius.route('/search', methods=['GET'])
def search():
    GENIUS_TOKEN = current_app.config['GENIUS_TOKEN']

    if request.method == 'GET':
        artist = request.args.get('artist')
        song = request.args.get('song')

        if not artist or not song:
            return jsonify({
                'data': None
            })

        genius = lyricsgenius.Genius(GENIUS_TOKEN)

        genius.verbose = False  # Turn off status messages
        genius.remove_section_headers = True  # Remove section headers (e.g. [Chorus]) from lyrics when searching
        genius.skip_non_songs = False  # Include hits thought to be non-songs (e.g. track lists)
        genius.excluded_terms = ["(Remix)", "(Live)"]  # Exclude songs with these words in their title

        song = genius.search_song(song, artist)

        res = {
            'artist': song.artist,
            'title': song.title,
            'image_url': song.song_art_image_url,
            'lyrics': song.lyrics
        }

        return jsonify({
            'data': res
        })


@genius.route('/recommended', methods=['GET'])
def get_recommended():
    SPOTIFY_CLIENT_ID = current_app.config['SPOTIFY_CLIENT_ID']
    SPOTIFY_CLIENT_SECRET = current_app.config['SPOTIFY_CLIENT_SECRET']

    if request.method == 'GET':
        client_id = SPOTIFY_CLIENT_ID
        client_secret = SPOTIFY_CLIENT_SECRET

        client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
        spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        results = spotify.new_releases(limit=8)['albums']['items']

        for k in results:
            print(k["name"])
            print(k["images"][0]["url"])
            print(k["external_urls"]["spotify"])

        res = [{
            'artist': r["artists"][0]["name"],
            'title': r["name"],
            'image_url': r["images"][0]["url"],
            'lyrics': r["external_urls"]["spotify"]
        } for r in results]

        return jsonify({
            'data': res
        })


@genius.route('/new_releases', methods=['GET'])
def get_new_releases():
    SPOTIFY_CLIENT_ID = current_app.config['SPOTIFY_CLIENT_ID']
    SPOTIFY_CLIENT_SECRET = current_app.config['SPOTIFY_CLIENT_SECRET']

    if request.method == 'GET':
        limit = request.args.get('limit')
        offset = request.args.get('offset')

        args = {
            'limit': limit if limit else 20,
            'offset': offset if offset else 0
        }

        client_id = SPOTIFY_CLIENT_ID
        client_secret = SPOTIFY_CLIENT_SECRET

        client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
        spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        results = spotify.new_releases(**args)['albums']['items']

        res = [i['name'] for i in results]

        return jsonify({
            'data': res
        })
