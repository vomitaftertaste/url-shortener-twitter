from peewee import *
from config import get_config

db = SqliteDatabase(get_config('DATABASE'))

class UrlData(Model):
    short = CharField(unique = True)
    full = CharField()
    
    class Meta:
        database = db

class KeyValueItem(Model):
    key = CharField(unique = True)
    value = CharField()
    
    class Meta:
        database = db

db.create_tables([UrlData,KeyValueItem], safe=True)