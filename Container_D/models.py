from peewee import Model, IntegerField, TextField, PrimaryKeyField
from db import db
class Artist(Model):
    id = PrimaryKeyField()
    name = TextField()
    genre = TextField()
    image_link = TextField()
    bio = TextField()

    class Meta:
        database = db
        table_name = 'Artist'

class Album(Model):
    id = PrimaryKeyField()
    title = TextField()
    artist = TextField()
    genre = TextField()
    art = TextField()

    class Meta:
        database = db
        table_name = 'Album'

class Track(Model):
    id = PrimaryKeyField()
    number = IntegerField()
    title = TextField()
    artist = TextField()
    album = TextField()
    duration = TextField()

    class Meta:
        database = db
        table_name = 'Track'