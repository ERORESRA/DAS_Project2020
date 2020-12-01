from flask import Flask, render_template, redirect, request
from flask.wrappers import Response
from data_getter import *
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/artist',methods=['GET', 'POST'])
def search_the_artist():
    if request.method == 'POST':
        artist=request.form['name'].replace(' ','+')
        return redirect('/artist/'+artist)
    else:   
        return render_template('/searchers/artist.html')

@app.route('/artist/<_name>')
def get_the_artist_by_name(_name:str):
    _name = _name.replace('+',' ')
    _artist = get_artist_by_name(_name)
    _albums = get_albums_by_artist(_name)
    return render_template('/results/artist_result.html', musician=_artist, albums=_albums)

@app.route('/album',methods=['GET', 'POST'])
def search_the_album():
    if request.method == 'POST':
        album=request.form['title'].replace(' ','+')
        return redirect('/album/'+album)
    else:   
        return render_template('/searchers/album.html')

@app.route('/album/<_title>')
def get_the_album_by_title(_title:str):
    _title = _title.replace('+',' ')
    _album = get_album_by_title(_title)
    _tracks = get_tracks_by_album_title(_title)
    return render_template('/results/album_result.html', _album=_album, _tracks=_tracks)

@app.route('/track/',methods=['GET', 'POST'])
def search_the_track():
    if request.method == 'POST':
        track=request.form['title'].replace(' ','+')
        return redirect('/track/'+track)
    else:   
        return render_template('/searchers/track.html')

@app.route('/track/<_title>')
def get_the_track_by_title(_title:str):
    _title = _title.replace('+',' ')
    _track = get_track_by_title(_title)
    return render_template('/results/track_result.html', _track=_track)

@app.route('/about')
def about_the_app():
    return render_template('about.html')


@app.route('/artist/_everyone_')
def get_all_artists_from_db():
    _everyone = get_all_artists()
    return render_template('/results/artist_everyone.html', everyone=_everyone)

@app.route('/album/_all_')
def get_all_albums_from_db():
    _every_album = get_all_albums()
    return render_template('/results/albums_everything.html', albums=_every_album)

@app.route('/track/_all_')
def get_all_tracks_from_db():
    _every_track = get_all_tracks()
    return render_template('/results/tracks_everything.html', tracks=_every_track)

@app.route('/api/artist/<_artist>',methods=['POST'])
def api_get_artist(_artist:str):
    _artist = _artist.replace('+',' ')
    the_artist = get_artist_by_name(_artist)
    return json.dumps(the_artist, indent=2)
@app.route('/api/album/<_album>/',methods=['POST'])
def api_get_album(_album:str):
    _album = _album.replace('+',' ')
    the_album = get_album_by_title(_album)
    the_tracks = get_tracks_by_album_title(_album)
    the_album['tracks'] = the_tracks
    return json.dumps(the_album, indent=2)
@app.route('/api/track/<_track>',methods=['POST'])
def api_get_track(_track:str):
    _track = _track.replace('+',' ')
    the_track = get_track_by_title(_track)
    return json.dumps(the_track, indent=2)
@app.route('/api/artist/all',methods=['POST'])
def api_get_every_artist():
    _the_artists = get_all_artists()
    return json.dumps(_the_artists)
@app.route('/api/album/all',methods=['POST'])
def api_get_every_album():
    _the_albums = get_all_albums()
    return json.dumps(_the_albums)
@app.route('/api/track/all',methods=['POST'])
def api_get_every_track():
    _the_tracks = get_all_tracks()
    return json.dumps(_the_tracks)
@app.route('/api/album/<_artist>',methods=['POST'])
def api_get_albums_by_artist(_artist:str):
    _artist = _artist.replace('+',' ')
    the_albums = get_albums_by_artist(_artist)
    return json.dumps(the_albums, indent=2)
@app.route('/api/track/<_album>',methods=['POST'])
def api_get_tracks_by_album(_album:str):
    _album = _album.replace('+',' ')
    the_albums = get_tracks_by_album_title(_album)
    return json.dumps(the_albums, indent=2)

@app.route('/api/artist_by_id/<_id>',methods=['POST'])
def api_get_artist_by_id(_id:str):
    _id = int(_id)
    the_artist = get_artist_by_id(_id)
    return json.dumps(the_artist, indent=2)
@app.route('/api/album_by_id/<_id>/',methods=['POST'])
def api_get_album_by_id(_id:str):
    _id = int(_id)
    the_album = get_album_by_id(_id)
    the_tracks = get_tracks_by_album_title(the_album['title'])
    the_album['tracks'] = the_tracks
    return json.dumps(the_album, indent=2)
@app.route('/api/track_by_id/<_id>',methods=['POST'])
def api_get_track_by_id(_id:str): 
    _id = int(_id)
    the_track = get_track_by_id(_id)
    return json.dumps(the_track, indent=2)



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
