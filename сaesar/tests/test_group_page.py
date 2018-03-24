from tests.test_base import TestBase
from front.pages.login_page import LogInPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time

import unittest

expected_url = 'http://localhost:3000/Groups/Dnipro'


class TestGroupPage(TestBase):

    def test_group_location(self):
        """При входе как админ по умолчанию попадаем в окно с локацией 'Dnipro' это и проверяем, протестировано"""
        groups_page = LogInPage(self.driver) \
            .user_name("hello") \
            .user_password('1234') \
            .submit_log_in()
        expected_result = 'Dnipro'
        group_location = WebDriverWait(self.driver, 10).until(lambda driver: groups_page.group_location())
        self.assertEqual(groups_page.get_current_url(), expected_url)
        self.assertEqual(expected_result, group_location)

    def test_is_enabled_button_search(self):
        """Доступна ли кнопка поиска, хотя она ничего не далает(("""
        groups_page = LogInPage(self.driver) \
            .user_name("hello") \
            .user_password('1234') \
            .submit_log_in()
        button_search = WebDriverWait(self.driver, 10).until(lambda driver: groups_page.button_search())
        assert button_search.is_enabled()

    def test_is_enable_button_my_groups(self):
        """Доступна ли кнопка myGroups"""
        groups_page = LogInPage(self.driver) \
            .user_name("hello") \
            .user_password('1234') \
            .submit_log_in()
        button_my_groups = WebDriverWait(self.driver, 10).until(lambda driver: groups_page.button_my_groups())
        assert button_my_groups.is_enabled()

    def test_is_enable_button_all_groups(self):
        """Доступна ли кнопка allGroups, но она есть и невидима, и странно чт тест проходт!"""
        groups_page = LogInPage(self.driver) \
            .user_name("hello") \
            .user_password('1234') \
            .submit_log_in()
        button_all_groups = WebDriverWait(self.driver, 10).until(lambda driver: groups_page.button_all_groups())
        assert button_all_groups.is_enabled()

    def test_is_enable_button_ended_groups(self):
        """Доступна ли кнопка ended_groups"""
        groups_page = LogInPage(self.driver) \
            .user_name("hello") \
            .user_password('1234') \
            .submit_log_in()
        button_ended_groups = WebDriverWait(self.driver, 10).until(lambda driver: groups_page.button_ended_groups())
        assert button_ended_groups.is_enabled()

    def test_is_enable_button_current_groups(self):
        """Доступна ли кнопка current_groups"""
        groups_page = LogInPage(self.driver) \
            .user_name("hello") \
            .user_password('1234') \
            .submit_log_in()
        button_current_groups = WebDriverWait(self.driver, 10).until(lambda driver: groups_page.button_current_groups())
        assert button_current_groups.is_enabled()

    def test_is_enable_button_future_groups(self):
        """Доступна ли кнопка future_groups"""
        groups_page = LogInPage(self.driver) \
            .user_name("hello") \
            .user_password('1234') \
            .submit_log_in()
        button_future_groups = WebDriverWait(self.driver, 10).until(lambda driver: groups_page.button_future_groups())
        assert button_future_groups.is_enabled()

    # def test_is_enable_button_create_group(self):
    #     """Доступна ли кнопка create_group, доработать"""
    #     groups_page = LogInPage(self.driver) \
    #         .user_name("hello") \
    #         .user_password('1234') \
    #         .submit_log_in()
    #     time.sleep(10)
    #     element_to_hover_over = groups_page.left_bar()
    #     left_bar = ActionChains(self.driver).move_to_element(element_to_hover_over)
    #     left_bar.perform()
    #     print('ok')
    #     create_group = WebDriverWait(self.driver, 10).until(lambda driver: groups_page.create_group())
    #     print('ok')
    #     assert create_group.is_enabled()

    # def test_right_bar_button(self):
    #     """Тест кликабельна ли кнопка right_bar. доработать"""
    #     groups_page = LogInPage(self.driver) \
    #         .user_name("hello") \
    #         .user_password('1234') \
    #         .submit_log_in()
    #     time.sleep(10)
    #     assert groups_page.open_right_bar().is_enabled()


    def test_groups_list(self):
        """Список групп на текущей странице, протстировано"""
        groups_page = LogInPage(self.driver) \
            .user_name("hello") \
            .user_password('1234') \
            .submit_log_in()
        time.sleep(10)
        expected_list_group = ['DP-093-JS', 'DP-094-MQC']
        actual_list_group = WebDriverWait(self.driver, 10).until(lambda driver: groups_page.groups_list())
        self.assertEqual(actual_list_group, expected_list_group)


if __name__ == '__main__':
    unittest.main()
