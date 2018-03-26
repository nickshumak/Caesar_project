import time


class User(object):
    # def __init__(self, login, password) -> None:
    def __init__(self, first_name, last_name, role, location, login, password) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.location = location
        self.login = login
        self.password = password

    def auto_login(self, login_page):
        """

        This function auto login user and open Group page
        :param login_page:
        """
        login_page.login = self.login
        login_page.password = self.password
        login_page.submit.click()
        time.sleep(2)


first_admin = User("Kirill", "Kozak", "Administrator", "Dnipro", "qwerty", "1234")
teacher = User("Olexandr", "Reuta", "Teacher", "Dnipro", "sasha", "1234")
coordinator = User("Dmytro", "Petin", "Coordinator", "Dnipro", "dmytro", "1234")
