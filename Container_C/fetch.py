import requests
import json
from creators import Artist_Creator,Album_Creator,Track_Creator
from models import *
from json_consumer import *
import time

def bring_artist_from_api(artist:str,key:str):
    artist = str(artist)
    artist = artist.replace(' ','+')
    url = f'http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist={artist}&api_key={key}&format=json'
    json_data = requests.get(url)
    data = json.loads(json_data.content)
    time.sleep(0.5)
    return data
def bring_album_from_api(artist:str,album:str,key:str):
    artist = str(artist)
    album = str(album)
    artist = artist.replace(' ','+')
    album = album.replace(' ','+')
    url = f'http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={key}&artist={artist}&album={album}&format=json'
    json_data = requests.get(url)
    data = json.loads(json_data.content)
    time.sleep(0.5)
    return data


def insert_artist(_artist:Artist):
    try:
        _artist.save(force_insert=True)
        print(f"Se inserto a: {_artist.name}")
    except Exception as e:
        print(f"Hubo un error al insertar el registro de: {_artist.name}, no se inserto en la BD")
        print(e)
def insert_album(_album:Album):
    try:
        _album.save(force_insert=True)
    except:
        print(f"Hubo un error al insertar el registro de: {_album.title}, no se inserto en la BD")
def insert_track(_track:Track):
    try:
        _track.save(force_insert=True)
    except:
        print(f"Hubo un error al insertar el registro de: {_track.title}, no se inserto en la BD")


def main():
    time.sleep(180)
    key = get_api_key()
    print("Se va a scrapear la api, tomara algo de tiempo.....")
    
    _artists = get_artist_from_file()
    _the_artists = []
    _albums = get_albums_from_file()
    _the_albums=[]
    _the_tracks=[]
    print("Se van a scrapear artistas")
    for x in range(len(_artists)):
        data_artist = bring_artist_from_api(_artists[x].get('Artist'),key) 
        Actual_Artist = Artist_Creator(data_artist.get('artist'))
        print(Actual_Artist.name)
        print(Actual_Artist.bio)
        _the_artists.append(Actual_Artist)

    print("Se van a scrapear albumes y track")
    for y in range(len(_albums)):
        print(f'\n{_albums[y]["Album"]} se va scrapear')
        data_album = bring_album_from_api(_albums[y].get('Artist'),_albums[y].get('Album'),key)
        Actual_Album = Album_Creator(data_album.get('album'))
        print(Actual_Album.title)
        print(Actual_Album.artist)
        _the_albums.append(Actual_Album)
        tracks = Track_Creator(data_album.get('album'))
        for y2 in range(len(tracks)):
            _the_tracks.append(tracks[y2])
    
    print('Los tracks que se scrapearon son:\n')
    for track in _the_tracks:
        print(f'{track.number} - {track.title} - {track.artist}')
        

    try:
        Artist.bulk_create(_the_artists)
    except Exception as e:
        print(f'Ha ocurrido un error y no se han registrado los datos el error es:\n{e}')
    try:
        Album.bulk_create(_the_albums)
    except Exception as e:
        print(f'Ha ocurrido un error y no se han registrado los datos el error es:\n{e}')
    try:
        Track.bulk_create(_the_tracks)
    except Exception as e:
        print(f'Ha ocurrido un error y no se han registrado los datos el error es:\n{e}')


if __name__ == "__main__":
    main()
    pass