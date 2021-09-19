import requests
import time
import sys
import serial
PORT = 'COM3'
from pprint import pprint
 
 
SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
ACCESS_TOKEN = 'BQASz_PrfZ63T91lvpE-FYJZUhhWeboJ8epXVx2J3Ys3qgIffch3oKbFXHZEWgYzBWtlrLQbX-IpjUuddQLuurkUxITdbxbTWqTZBH-aJMaKHeX0R11f26KywOLut5rR5ypPEwsDO-Hy6NEsk8rp6E68BmTMQB4xoXiJX-IT'
 
def get_current_track(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    json_resp = response.json()
 
    track_id = json_resp['item']['id']
    track_uri = json_resp['item']['uri']
    track_name = json_resp['item']['name']
    artists = [artist for artist in json_resp['item']['artists']]
    artist_id = ', '.join([artist['id'] for artist in artists])

    SPOTIFY_GET_ARTIST = f"https://api.spotify.com/v1/artists/{artist_id}"
    artist_response = requests.get(
        SPOTIFY_GET_ARTIST, 
        headers={
            "Authorization": f"Bearer {access_token}"
        } 
    )
    json_resp2 = artist_response.json()
    genre = json_resp2.get("genres")[0]
 
    current_track_info = {
        "id": track_id,
        "track uri": track_uri,
        "artist id": artist_id,
        "track name": track_name,
        "genre": genre
    }
 
    return current_track_info

#API requests
def main():

    current_track_id = None
    while True:
        current_track_info = get_current_track(ACCESS_TOKEN)
        song_genre = current_track_info.get("genre")
        print(song_genre)
 
        if current_track_info['id'] != current_track_id:
            pprint(
                current_track_info,
                indent=4,
            )
            current_track_id = current_track_info['id']

            ser = serial.Serial('COM3', 9800, timeout=1)
            time.sleep(2)

        while(True):
            if(song_genre == "modern rock"):
                ser.writelines(b'H')   # send a byte
                time.sleep(0.1)        # wait 0.5 seconds
                ser.writelines(b'L')   # send a byte
                time.sleep(0.05)
            if(song_genre == "hip hop"):
                ser.writelines(b'H')   # send a byte
                time.sleep(0.5)        # wait 0.5 seconds
                ser.writelines(b'L')   # send a byte
                time.sleep(0.5)
            if(song_genre == "pop"):
                ser.writelines(b'H')   # send a byte
                time.sleep(1)        # wait 0.5 seconds
                ser.writelines(b'L')   # send a byte
                time.sleep(1)
            if(song_genre == "contemporary country"):
                ser.writelines(b'H')   # send a byte
                time.sleep(2)        # wait 0.5 seconds
                ser.writelines(b'L')   # send a byte
                time.sleep(2)

            current_track_info = get_current_track(ACCESS_TOKEN)
            song_genre = current_track_info.get("genre")

            if current_track_info['id'] != current_track_id:
                pprint(
                current_track_info,
                indent=4,
            )
            current_track_id = current_track_info['id']
        

        ser.close()
 
if __name__ == '__main__':
    args = sys.argv
    try:
        main(args[1])
    except IndexError:
        main()
