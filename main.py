from datab import Original
from peewee import *
import telebot
import random
from operator import itemgetter
from ttepars import sl

bot = telebot.TeleBot('6248167598:AAHMk_rLZhLoOTbsEknbEKROGI1KrwR6f_0')


@bot.message_handler(commands=["Originals"])
def get_text_messages(message):
    spicok = []
    query = Original.get()
    for elem in query.select().order_by(Original.IMDB_Score.desc()).limit(100):                         #.where(Original.Runtime >70).order_by(fn.Random()).order_by(Original.Runtime):

        apper = [elem.Title, elem.Genre, elem.IMDB_Score]
        spicok.append(apper)
    b = random.sample(spicok, 5)

    e = sorted(b, key=itemgetter(2), reverse=True)
    
    for i in e:
        buf = ""
        for elm in i:
            buf = buf + str(elm) + ' '
        bot.send_message(message.from_user.id,str(buf)) 

    # for i in b:
    #     buf = ""
    #     for elemr in i:
    #         buf = buf + str(i) + " "
    #     print(buf)
       
@bot.message_handler(content_types=["text"])
def filter_message(message):
    spicok = []
    text = message.text.split("/")
    p = 1
    for name in text:
        p = p * sl.get(name,1 )
    query = Original.get()                 #Original.Genre%p == 0
    print(p)
    for elem in query.select():                         #.where(Original.Runtime >70).order_by(fn.Random()).order_by(Original.Runtime):

        apper = [elem.Title, elem.Genre, elem.IMDB_Score]
        spicok.append(apper)

    new_spisok = []
    for i in spicok:
        if i[1]%p == 0:
            new_spisok.append(i.copy())

    b = random.sample(new_spisok, 5)
    print(new_spisok)
    e = sorted(b, key=itemgetter(2), reverse=True)
    
    for i in e:
        buf = ""
        for elm in i:
            buf = buf + str(elm) + ' '
        print(buf)
        bot.send_message(message.from_user.id,str(buf)) 



bot.polling(none_stop=True, interval=0)

# spicok = []
# text = input(": ").split("/")
# p = 1
# for name in text:
#     p = p * sl.get(name,1 )
# query = Original.get()                 #Original.Genre%p == 0
# print(p)
# for elem in query.select():                         #.where(Original.Runtime >70).order_by(fn.Random()).order_by(Original.Runtime):

#     apper = [elem.Title, elem.Genre, elem.IMDB_Score]
#     spicok.append(apper)

# new_spisok = []
# for i in spicok:
#     if i[1]%p == 0:
#         new_spisok.append(i.copy())

# b = random.sample(new_spisok, 5)
# print(new_spisok)
# e = sorted(b, key=itemgetter(2), reverse=True)
    
# for i in e:
#     buf = ""
#     for elm in i:
# #         buf = buf + str(elm) + ' '
# #     print(buf)





# def print_ganre():
#     print(sl)

# print_ganre()
