from operator import truediv, truth
from models import *

def Artist_Creator(artist:dict):
    _artist = Artist()
    _artist.name = artist.get('name')
    _artist.genre = artist.get('tags').get('tag')[0].get('name')
    _artist.image_link = artist.get('image')[4].get('#text')
    _artist.bio = artist.get('bio').get('summary')
    return _artist

def Album_Creator(album:dict):
    _Album = Album(
    title = album.get('name'),
    artist = album.get('artist'),
    genre = album.get('tags').get('tag')[0].get('name'),
    art = album.get('image')[5].get('#text'))
    return _Album

def Track_Creator(album:dict):
    _tracks = []
    for x in range(len(album.get('tracks').get('track'))):
        _track = Track(
        number = x+1,
        title = album.get('tracks').get('track')[x].get('name'),
        artist = album.get('artist'),
        album = album.get('name'),
        duration = album.get('tracks').get('track')[x].get('duration')
            )
        _tracks.append(_track)
    return _tracks


if __name__ == "__main__":
    print('test')
