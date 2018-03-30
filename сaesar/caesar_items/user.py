class User(object):
    def __init__(self, first_name, last_name, role, location, login, password) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.location = location
        self.login = login
        self.password = password
        self.full_name = first_name + '\n' + last_name






