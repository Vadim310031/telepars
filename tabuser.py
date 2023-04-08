from peewee import *

db = SqliteDatabase('users.db')

class User(Model):
    Login = CharField()
    Password = CharField()
    Role = CharField()
    Email = CharField()
    class Meta:
        database = db 
if __name__ == "__main__":  
    User.create_table()
    User.create(Login = "545", Password ="123456789", Role = "root", Email ="kloynPY@gmail.com")

