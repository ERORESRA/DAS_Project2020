from peewee import Model, CharField, IntegerField, TextField
from db import db
class Artist(Model):
    id = IntegerField()
    name = TextField()
    genre = TextField()
    image_link = TextField()
    bio = TextField()

    class Meta:
        database = db
        table_name = 'Artist'

class Album(Model):
    id = IntegerField()
    title = TextField()
    artist = TextField()
    genre = TextField()
    art = TextField()

    class Meta:
        database = db
        table_name = 'Album'

class Track(Model):
    number = IntegerField()
    title = TextField()
    artist = TextField()
    album = TextField()

    class Meta:
        database = db
        table_name = 'Track'