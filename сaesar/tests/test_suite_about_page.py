from tests.test_base import TestBase
from resource.users_base import first_admin


class TestAboutPage(TestBase):
    def setUp(self):
        super().setUp()
        self.group_page = self.login_page.auto_login(first_admin)
        self.top_menu = self.group_page.open_top_menu()
        self.about_page = self.top_menu.click_about_button()

    def test01_open_development_panel(self):
        """
        Check that user can open development & research
        :return:
        """
        expected_result = 'Development & Research'
        self.about_page.development_research_button().click()
        self.assertTrue(self.about_page.team_doloto_icon().is_displayed())
        self.assertEqual(self.about_page.get_department_text(), expected_result)

    def test02_open_quality_assurance_panel(self):
        """
        Check that user can open quality assurance
        :return:
        """
        expected_result = 'Quality Assurance'
        self.about_page.quality_assurance_button().click()
        self.assertTrue(self.about_page.light_side_icon().is_displayed())
        self.assertEqual(self.about_page.get_department_text(), expected_result)

    def test03_open_management_panel(self):
        """
        Check that user can open quality assurance
        :return:
        """
        expected_result = 'Management and Mentoring'
        self.about_page.management_button().click()
        self.assertEqual(self.about_page.get_department_text(), expected_result)

    def test04_open_additional_thanks_panel(self):
        """
        Check that user can open quality assurance
        :return:
        """
        expected_result = 'Additional Thanks'
        self.about_page.additional_thanks_button().click()
        self.assertEqual(self.about_page.get_department_text(), expected_result)



