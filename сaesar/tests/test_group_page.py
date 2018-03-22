from tests.test_base import TestBase
from front.pages.login_page import LogInPage
from selenium.webdriver.common.action_chains import ActionChains
import time

import unittest


class TestGroupPage(TestBase):

    def test_group_location(self):
        """При входе как админ по умолчанию попадаем в окно с локацией 'Dnipro' это и проверяем, протестировано"""
        groups_page = LogInPage(self.driver) \
            .user_name("hello") \
            .user_password('1234') \
            .submit_log_in()
        time.sleep(10)
        # self.assertEqual(groups_page.getCurrentUrl(), 'localhost:3000/Groups/Dnipro')
        expected_result = 'Dnipro'
        group_location = groups_page.group_location()
        self.assertEqual(expected_result, group_location)

    def test_is_enabled_button_search(self):
        """Доступна ли кнопка поиска, хотя она ничего не далает(("""
        groups_page = LogInPage(self.driver) \
            .user_name("hello") \
            .user_password('1234') \
            .submit_log_in()
        time.sleep(10)
        assert groups_page.button_search().is_enabled()

    def test_is_enable_button_my_groups(self):
        """Доступна ли кнопка myGroups"""
        groups_page = LogInPage(self.driver) \
            .user_name("hello") \
            .user_password('1234') \
            .submit_log_in()
        time.sleep(10)
        assert groups_page.button_my_groups().is_enabled()

    def test_is_enable_button_all_groups(self):
        """Доступна ли кнопка allGroups, но она есть и невидима, и странно чт тест проходт!"""
        groups_page = LogInPage(self.driver) \
            .user_name("hello") \
            .user_password('1234') \
            .submit_log_in()
        time.sleep(10)
        assert groups_page.button_all_groups().is_enabled()

    def test_is_enable_button_ended_groups(self):
        """Доступна ли кнопка ended_groups"""
        groups_page = LogInPage(self.driver) \
            .user_name("hello") \
            .user_password('1234') \
            .submit_log_in()
        time.sleep(10)
        assert groups_page.button_ended_groups().is_enabled()

    def test_is_enable_button_current_groups(self):
        """Доступна ли кнопка current_groups"""
        groups_page = LogInPage(self.driver) \
            .user_name("hello") \
            .user_password('1234') \
            .submit_log_in()
        time.sleep(10)
        assert groups_page.button_current_groups().is_enabled()

    def test_is_enable_button_future_groups(self):
        """Доступна ли кнопка future_groups"""
        groups_page = LogInPage(self.driver) \
            .user_name("hello") \
            .user_password('1234') \
            .submit_log_in()
        time.sleep(10)
        assert groups_page.button_future_groups().is_enabled()

    def test_is_enable_button_create_group(self):
        """Доступна ли кнопка create_group"""
        groups_page = LogInPage(self.driver) \
            .user_name("hello") \
            .user_password('1234') \
            .submit_log_in()
        time.sleep(10)
        element_to_hover_over = groups_page.left_bar()
        left_bar = ActionChains(self.driver).move_to_element(element_to_hover_over)
        time.sleep(5)
        left_bar.perform()
        print('ok')
        create_group = groups_page.create_group()
        print('ok')
        assert groups_page.create_group().is_enabled()

    def test_right_bar_button(self):
        """Тест кликабельна ли кнопка right_bar, дописать увеличение размеров окна, тогда не будет падать тест"""
        groups_page = LogInPage(self.driver) \
            .user_name("hello") \
            .user_password('1234') \
            .submit_log_in()
        time.sleep(10)
        assert groups_page.open_right_bar()


    # def test_groups_list(self):
    #     """Список групп на текущей странице"""
    #     groups_page = LogInPage(self.driver) \
    #         .user_name("hello") \
    #         .user_password('1234') \
    #         .submit_log_in()
    #     time.sleep(10)
    #     groups_list = groups_page.groups_list()
    #     print(groups_list)
    #     # self.assertEqual('Dnipro', group_location)
    #     time.sleep(10)



if __name__ == '__main__':
    unittest.main()
