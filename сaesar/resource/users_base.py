
from caesar_items.user import User

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
user_password_length_4 = User("", "", "", "", "vasya3", "1234")
user_password_length_11 = User("", "", "", "", "vasya2", "12345678901")
user_password_length_10 = User("", "", "", "", "vasya", "1234567890")
user_login_length_3 = User("", "", "", "", "vas", "1234")
user_login_length_4 = User("", "", "", "", "vasy", "1234")
user_login_length_10 = User("", "", "", "", "vasyavasya", "1234")
user_login_length_11 = User("", "", "", "", "vasyavasyvasya1", "1234")