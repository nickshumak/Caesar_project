from front.pages.admin_page import *
from front.user import User

"""
This file contains users on whose behalf the testing will be conducted
Этот файл содержит пользователей, от имени которых будет проводиться 
    тестирование
"""

first_admin = User("Kirill", "Kozak", "ITA Administrator", "Dnipro", "qwerty", "1234")
second_admin = User("Petr", "Kucher", "ITA Administrator", "Dnipro", "hello", "1234")
third_admin = User("Andriy", "Pereymybida", "ITA Administrator", "Lviv", "admin", "1234")
fourth_admin = User("Artur", "Koval", "ITA Administrator", "Dnipro", "artur", "1234")
coordinator = User("Dmytro", "Petin", "ITA Coordinator", "Dnipro", "dmytro", "1234")
teacher = User("Olexandr", "Reuta", "ITA Teacher", "Dnipro", "sasha", "1234")
user_password_length_3 = User("", "", "", "", "vasya1", "123")
user_password_length_4 = User("", "", "", "", "petya", "1234")
user_password_length_11 = User("", "", "", "", "vasya2", "12345678901")
user_password_length_10 = User("", "", "", "", "vasya", "1234567890")
user_login_length_3 = User("", "", "", "", "vas", "1234")
user_login_length_4 = User("", "", "", "", "vasy", "1234")
user_login_length_10 = User("", "", "", "", "vasyavasya", "1234")
user_login_length_11 = User("", "", "", "", "vasyavasyvasya1", "1234")


def create_8_users_for_tests(driver):
    AdminPage(driver). \
        get_page("http://localhost:3000/admin").tab_users() \
        .add_entity_user().fill_user_fields(
        '', "", "Teacher", "Dnipro", "", user_login_length_3.login, user_login_length_3.password)
    AdminPage(driver). \
        get_page("http://localhost:3000/admin").tab_users() \
        .add_entity_user().fill_user_fields(
        '', "", "Teacher", "Dnipro", "", user_login_length_4.login, user_login_length_4.password)
    AdminPage(driver). \
        get_page("http://localhost:3000/admin").tab_users() \
        .add_entity_user().fill_user_fields(
        '', "", "Teacher", "Dnipro", "", user_login_length_10.login, user_login_length_10.password)
    AdminPage(driver). \
        get_page("http://localhost:3000/admin").tab_users() \
        .add_entity_user().fill_user_fields(
        '', "", "Teacher", "Dnipro", "", user_login_length_11.login, user_login_length_11.password)
    AdminPage(driver). \
        get_page("http://localhost:3000/admin").tab_users() \
        .add_entity_user().fill_user_fields(
        '', "", "Teacher", "Dnipro", "", user_password_length_3.login, user_password_length_3.password)
    AdminPage(driver). \
        get_page("http://localhost:3000/admin").tab_users() \
        .add_entity_user().fill_user_fields(
        '', "", "Teacher", "Dnipro", "", user_password_length_4.login, user_password_length_4.password)
    AdminPage(driver). \
        get_page("http://localhost:3000/admin").tab_users() \
        .add_entity_user().fill_user_fields(
        '', "", "Teacher", "Dnipro", "", user_password_length_10.login, user_password_length_10.password)
    AdminPage(driver). \
        get_page("http://localhost:3000/admin").tab_users() \
        .add_entity_user().fill_user_fields(
        '', "", "Teacher", "Dnipro", "", user_password_length_11.login, user_password_length_11.password)
    driver.quit()
