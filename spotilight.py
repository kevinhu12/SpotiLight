import requests
import time
from pprint import pprint
 
 
SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
ACCESS_TOKEN = 'BQCOAzk2bAlh_rZ23N_JpjOIqzo16T3pkVfeNjut1zm0vmfi1pq7_OtFEEyVlHRicsXPzDLsoVDyDxtpDItaO580b_pKrgHS24T3PMmLRltCa_0gVkaRWCnagjD-1d98Ffloknmb9aAvWySDTPF_9ahw_Cv4BCAfw6g9Jq_1PQRHkO3sQrNH7LSAhn-Zc1OfsNTt3dfVDZIIJMYQcJ8C'
 
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
 
        if current_track_info['id'] != current_track_id:
            pprint(
                current_track_info,
                indent=4,
            )
            current_track_id = current_track_info['id']
 
        time.sleep(1)
 
if __name__ == '__main__':
    main()
