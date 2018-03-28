from caesar_items.user import User

"""
This file contains users on whose behalf the testing will be conducted
"""

first_admin = User("Kirill", "Kozak", "Administrator", "Dnipro",
                   "qwerty", "1234")
second_admin = User("Petr", "Kucher", "Administrator", "Dnipro",
                    "hello", "1234")
third_admin = User("Andriy", "Pereymybida", "Administrator", "Lviv",
                   "admin", "1234")
fourth_admin = User("Artur", "Koval", "Administrator", "Dnipro",
                    "artur", "1234")
coordinator = User("Dmytro", "Petin", "Coordinator", "Dnipro",
                   "dmytro", "1234")
teacher = User("Olexandr", "Reuta", "Teacher", "Dnipro", "sasha",
               "1234")
