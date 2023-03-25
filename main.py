from datab import Original
from peewee import *
import telebot
bot = telebot.TeleBot('6248167598:AAHMk_rLZhLoOTbsEknbEKROGI1KrwR6f_0')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id,"hi")


# query = Original.get(Original.IMDB_Score == 9)
# for elem in query.select().limit(10).where(Original.Runtime >70).order_by(fn.Random()).order_by(Original.Runtime):

#     print(elem.Title, elem.Genre, elem.Runtime)

bot.polling(none_stop=True, interval=0)