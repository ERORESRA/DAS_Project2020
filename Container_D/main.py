from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('artist/<artist_id>')
def get_the_artist(artist_id):
    artist = 0
    return render_template('artist.html', artist = artist)

@app.route('album/<album_id>')
def get_the_album(album_id):
    album = 0
    return render_template('album.html', album = album)

@app.route('track/<track_id>')
def get_the_track(track_id):
    track = 0
    return render_template('track.html', track = track)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
