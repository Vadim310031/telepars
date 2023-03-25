from peewee import *

db = SqliteDatabase('Netf.db')

class Original(Model):
    Title = CharField()
    Genre = CharField()
    Premiere = CharField()
    Runtime = IntegerField()
    IMDB_Score = FloatField()
    Language = CharField()



    class Meta:
        database = db 

Original.create_table()