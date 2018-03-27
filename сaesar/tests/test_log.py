from tests.test_base import TestBase
from caesar_items.pages.login_page import LogInPage
import time

import unittest


class TestLog(TestBase):

    # def test_login_in(self):
    #     """проверку добавить на факт нужной страницы"""
    #     groups_page = LogInPage(self.driver) \
    #         .user_name("dmytro") \
    #         .user_password('1234') \
    #         .submit_log_in().get_title_name()
    #     self.assertIn("Caesar", groups_page)
    #     time.sleep(5)

    def test_2(self):
        groups_page = LogInPage(self.driver) \
            .user_name("hello") \
            .user_password('1234') \
            .submit_log_in()
        time.sleep(5)
        group_location = groups_page.group_location()
        print(group_location)
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
