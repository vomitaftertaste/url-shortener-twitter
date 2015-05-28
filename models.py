from peewee import *
from config import get_config

db = SqliteDatabase(get_config('DATABASE'))

class UrlData(Model):
    short = CharField()
    full = CharField()
    
    class Meta:
        database = db
        
db.create_table(UrlData, safe=True)