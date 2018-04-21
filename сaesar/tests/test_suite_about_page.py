from selenium.webdriver.common.action_chains import ActionChains
from tests.test_base import TestBase
from resource.users_base import first_admin
from resource.error_handler import logger_exception


class TestAboutPage(TestBase):
    def setUp(self):
        super().setUp()
        self.group_page = self.login_page.auto_login(first_admin)
        self.top_menu = self.group_page.open_top_menu()
        self.about_page = self.top_menu.click_about_button()

    @logger_exception
    def test01_open_development_panel(self):
        """ Check that user can open development & research."""
        expected_result = 'Development & Research'
        self.about_page.development_research_button().click()
        self.assertTrue(self.about_page.team_doloto_icon().is_displayed())
        self.assertEqual(self.about_page.get_department_text(),
                         expected_result)

    @logger_exception
    def test02_open_quality_assurance_panel(self):
        """ Check that user can open quality assurance."""
        expected_result = 'Quality Assurance'
        self.about_page.quality_assurance_button().click()
        self.assertTrue(self.about_page.light_side_icon().is_displayed())
        self.assertEqual(self.about_page.get_department_text(),
                         expected_result)

    @logger_exception
    def test03_open_management_panel(self):
        """ Check that user can open quality assurance."""
        expected_result = 'Management and Mentoring'
        self.about_page.management_button().click()
        self.assertEqual(self.about_page.get_department_text(),
                         expected_result)

    @logger_exception
    def test04_open_additional_thanks_panel(self):
        """ Check that user can open quality assurance."""
        expected_result = 'Additional Thanks'
        self.about_page.additional_thanks_button().click()
        self.assertEqual(self.about_page.get_department_text(),
                         expected_result)

    @logger_exception
    def test05_open_development_team(self):
        """ Check that user can open and see development team."""
        self.about_page.development_research_button().click()
        self.about_page.team_doloto_icon().click()
        self.assertTrue(self.about_page.get_panel_with_photos().
                        is_displayed())

    @logger_exception
    def test06_open_qa_team(self):
        """ Check that user can open and see quality assurance team."""
        self.about_page.development_research_button().click()
        self.about_page.charming_chaos_icon().click()
        self.assertTrue(self.about_page.get_panel_with_photos().
                        is_displayed())

    @logger_exception
    def test07_check_that_name_changed_below_photo(self):
        """ Check that teammate name changed when user move mouse to
        another teammate."""
        self.about_page.development_research_button().click()
        self.about_page.charming_chaos_icon().click()
        photos = self.about_page.get_all_photos()
        last_teammate_name = ''
        for photo in photos:
            ActionChains(self.driver).move_to_element(photo).perform()
            current_teammate_name = self.about_page.get_teammate_name_text()
            self.assertNotEqual(last_teammate_name, current_teammate_name)
            last_teammate_name = current_teammate_name
