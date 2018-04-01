from caesar_items.pages.admin_page import *
from caesar_items.user import User
import time

"""
This file contains users on whose behalf the testing will be conducted
Этот файл содержит пользователей, от имени которых будет проводиться 
    тестирование
"""

first_admin =\
    User("Kirill", "Kozak", "ITA Administrator", "Dnipro", "qwerty", "1234")
second_admin =\
    User("Petr", "Kucher", "ITA Administrator", "Dnipro", "hello", "1234")
third_admin =\
    User("Andriy", "Pereymybida", "ITA Administrator", "Lviv", "admin", "1234")
fourth_admin =\
    User("Artur", "Koval", "ITA Administrator", "Dnipro", "artur", "1234")
coordinator =\
    User("Dmytro", "Petin", "ITA Coordinator", "Dnipro", "dmytro", "1234")
teacher = User("Olexandr", "Reuta", "ITA Teacher", "Dnipro", "sasha", "1234")
user_password_len_3 = User("", "", "", "", "vasya1", "123")
user_password_len_4 = User("", "", "", "", "petya", "1234")
user_password_len_11 = User("", "", "", "", "vasya2", "12345678901")
user_password_len_10 = User("", "", "", "", "vasya", "1234567890")
user_login_len_3 = User("", "", "", "", "vas", "1234")
user_login_len_4 = User("", "", "", "", "vasy", "1234")
user_login_len_10 = User("", "", "", "", "vasyavasya", "1234")
user_login_len_11 = User("", "", "", "", "vasyavasyvasya1", "1234")

users_set = (user_password_len_3, user_password_len_4,
             user_password_len_11, user_password_len_10,
             user_login_len_3, user_login_len_4,
             user_login_len_10, user_login_len_11)


def create_8_users_for_tests(driver):
    for user in users_set:
        admin_page = AdminPage(driver).add_entity_user()
        admin_page.fill_user_name(''). \
            fill_user_second_name(''). \
            fill_user_role_type('Teacher'). \
            fill_user_city('Dnipro'). \
            fill_user_photo(''). \
            fill_user_login(user.login). \
            fill_user_password(user.password). \
            submit()
        time.sleep(1)
