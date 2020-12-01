from models import Artist,Album,Track

def get_artist_by_id(_id:int):
    query = Artist.select().where(Artist.id == _id)
    try:
        _artist = {
            'id':query[0].id,
            'name':query[0].name,
            'genre':query[0].genre,
            'image_link':query[0].image_link,
            'bio':query[0].bio}
        return _artist
    except:
        _artist = {
            'id':0,
            'name':'not found',
            'genre':'not found',
            'image_link':'not found',
            'bio':'not found'}
        return _artist


def get_album_by_id(_id:int):
    query = Album.select().where(Album.id == _id)
    try:
        _album = {
            'id':query[0].id,
            'title':query[0].title,
            'artist':query[0].artist,
            'genre':query[0].genre,
            'art':query[0].art}
        return _album
    except:
        _album = {
            'id':0,
            'title':'not found',
            'artist':'not found',
            'genre':'not found',
            'art':'not found'}
        return _album
def get_track_by_id(_id:int):
    query = Track.select().where(Track.id == _id)
    try:
        _track = {
            'id':query[0].id,
            'number':query[0].number,
            'title':query[0].title,
            'artist':query[0].artist,
            'album':query[0].album,
            'duration':query[0].duration
            }
        return _track
    except:
        _track = {
            'id':0,
            'number':'not found',
            'title':'not found',
            'artist':'not found',
            'album':'not found',
            'duration':'not found'
            }
        return _track

def get_artist_by_name(_name:str):
    query = Artist.select().where(Artist.name == _name)
    try:
        _artist = {
            'id':query[0].id,
            'name':query[0].name,
            'genre':query[0].genre,
            'image_link':query[0].image_link,
            'bio':query[0].bio}
        return _artist
    except:
        _artist = {
            'id':0,
            'name':'not found',
            'genre':'not found',
            'image_link':'not found',
            'bio':'not found'}
        return _artist


def get_album_by_title(title:str):
    query = Album.select().where(Album.title == title)
    try:
        _album = {
            'id':query[0].id,
            'title':query[0].title,
            'artist':query[0].artist,
            'genre':query[0].genre,
            'art':query[0].art}
        return _album
    except:
        _album = {
            'id':0,
            'title':'not found',
            'artist':'not found',
            'genre':'not found',
            'art':'not found'}
        return _album

def get_track_by_title(title:str):
    query = Track.select().where(Track.title == title)
    try:
        _track = {
            'id':query[0].id,
            'number':query[0].number,
            'title':query[0].title,
            'artist':query[0].artist,
            'album':query[0].album,
            'duration':query[0].duration
            }
        return _track
    except:
        _track = {
            'id':0,
            'number':'not found',
            'title':'not found',
            'artist':'not found',
            'album':'not found',
            'duration':'not found'
            }
        return _track

def get_tracks_by_album_title(title:str):
    query = Track.select().where(Track.album == title)
    my_tracks = []
    for x in range(len(query)):
        try:
            _track = {
                'id':query[x].id,
                'number':query[x].number,
                'title':query[x].title,
                'artist':query[x].artist,
                'album':query[x].album,
                'duration':query[x].duration
                }
            my_tracks.append(_track) 
        except:
            _track = {
                'id':0,
                'number':'not found',
                'title':'not found',
                'artist':'not found',
                'album':'not found',
                'duration':'not found'
                }
            my_tracks.append(_track) 
    return my_tracks

def get_albums_by_artist(_artist:str):
    list_Album = Album.select().where(Album.artist == _artist)
    dicts_Album = []
    for x in range(len(list_Album)):
        try:
            _album = {
                'id':list_Album[x].id,
                'title':list_Album[x].title,
                'artist':list_Album[x].artist,
                'genre':list_Album[x].genre,
                'art':list_Album[x].art}
            dicts_Album.append(_album)
        except:
            _album = {
                'id':0,
                'title':'not found',
                'artist':'not found',
                'genre':'not found',
                'art':'not found'}
            dicts_Album.append(_album)
    return dicts_Album


def get_all_artists():
    list_Artist = Artist.select()
    dicts_Artist = []
    for x in range(len(list_Artist)):
        try:
            _artist = {
                'id':list_Artist[x].id,
                'name':list_Artist[x].name,
                'genre':list_Artist[x].genre,
                'image_link':list_Artist[x].image_link,
                'bio':list_Artist[x].bio}
            dicts_Artist.append(_artist)
        except:
            _artist = {
                'id':0,
                'name':'not found',
                'genre':'not found',
                'image_link':'not found',
                'bio':'not found'}
            dicts_Artist.append(_artist)
    return dicts_Artist

def get_all_albums():
    list_Album = Album.select()
    dicts_Album = []
    for x in range(len(list_Album)):
        try:
            _album = {
                'id':list_Album[x].id,
                'title':list_Album[x].title,
                'artist':list_Album[x].artist,
                'genre':list_Album[x].genre,
                'art':list_Album[x].art}
            dicts_Album.append(_album)
        except:
            _album = {
                'id':0,
                'title':'not found',
                'artist':'not found',
                'genre':'not found',
                'art':'not found'}
            dicts_Album.append(_album)
    return dicts_Album

def get_all_tracks():
    list_Track = Track.select()
    dicts_Track = []
    for x in range(len(list_Track)):
        try:
            _track = {
                'id':list_Track[x].id,
                'number':list_Track[x].number,
                'title':list_Track[x].title,
                'artist':list_Track[x].artist,
                'album':list_Track[x].album,
                'duration':list_Track[x].duration
                }
            dicts_Track.append(_track)
        except:
            _track = {
                'id':0,
                'number':'not found',
                'title':'not found',
                'artist':'not found',
                'album':'not found',
                'duration':'not found'
                }
            dicts_Track.append(_track)
    return dicts_Track

