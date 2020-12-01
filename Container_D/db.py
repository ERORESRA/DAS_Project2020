import os
from os import name
from peewee import MySQLDatabase

DATABASE = {
    'HOST': os.getenv('DB_HOST'),
    'PORT': os.getenv('DB_PORT'),
    'DATABASE': os.getenv('DB_NAME'),
    'USER': os.getenv('DB_USER'),
    'PASSWORD': os.getenv('DB_PASSWORD'),
}
db = MySQLDatabase(
    user=DATABASE['USER'],
    password=DATABASE['PASSWORD'],
    host=DATABASE['HOST'],
    database=DATABASE['DATABASE'],
    port = int(DATABASE['PORT'])
)