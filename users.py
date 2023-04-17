from tabuser import User
import re
from rr import pasword
from peewee import *
def email_chek(email):

    pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"

    if re.match(pattern, email) is not None:
        return True
    else:
        return False





i = int(input("1-Авторизация\n2-Регистрация\nВведите число:  "))
if i == 1:
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    
    One = User.select().where(User.Login == login).get()

    print(One['Login'])











elif i == 2:
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    email = input("Введите емаил: ")

    if email_chek(email) == True:
        
        User.create(Login = login, Password = password, Email = email, Role = "User")







else:
    print("0101001")


