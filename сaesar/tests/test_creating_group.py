import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from front.pages.groups_page import GroupsPage
from resource.users_base import first_admin
from tests.test_base import TestBase

TEST_GROUP_NAME = "Test group"


class TestCreatingGroup(TestBase):

    def test_open_create_page(self):
        first_admin.auto_login_n_open_group_page(self.login_page)
        groups_page = GroupsPage(self.driver)
        left_menu = groups_page.left_menu_open()
        time.sleep(2)
        left_menu.create_group().click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "name")))
        groups_page.WindowCreatingGroup().direction_of_group_choosing(2)
        groups_page.WindowCreatingGroup().location_of_group_choosing()
        groups_page.WindowCreatingGroup().group_name_setting(TEST_GROUP_NAME)
        test_direction = groups_page.WindowCreatingGroup().direction_of_group_save_to_variable()
        groups_page.WindowCreatingGroup().group_name_setting(TEST_GROUP_NAME)

        time.sleep(5)
        # self.assertEqual(self.driver.current_url, expected_page_url)


class CommentsList(object):
    """
    Class to find the required elements on all pages of the site
    """

    def __init__(self, web_driver):
        self.__driver = web_driver

    def search_by_comment(self) -> list:

        """
        Function-finder the required elements on all pages by entered comment
        :return:
        """

        list_el = self.__driver.find_element_by_class_name(
            "small-group-view col-md-6")
        list_a = list_el.find_elements_by_tag_name("p")
        href = set()
        text_columns = list()
        for link_a in list_a:
            href.add(link_a.get_attribute("href"))

        for ref in href:
            self.__driver.get(ref)
            list_columns = self.__driver.find_elements_by_class_name(
                "textcolumn")
            for column in list_columns:
                text_columns.append(column.text)

        return text_columns
