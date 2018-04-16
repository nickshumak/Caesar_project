"""
Tests check the adding, removal and editing of
student data, adding cv_files and photo in the list of students
with different roles(administrator, coordinator, teacher),
also check the opportunity of adding new student with empty data and
sorting student's list by name.
"""

import unittest
import logging
from caesar_items.pages.groups_page import GroupsPage
from caesar_items.pages.students_page import StudentsPage,\
    data_student_for_check, remove_none_from_list
from resource.users_base import first_admin, coordinator, teacher
from tests.test_base_set_up_class import TestBaseSetUP
from tests.test_base import TestBase
from resource.data_for_test_suit_students_page import data


logging.basicConfig(filename='test.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


class TestStudentsPageWithAdmin(TestBaseSetUP):
    driver = None

    @classmethod
    def setUpClass(cls, user='', group=''):
        """ Log in as administrator, open top menu,select
        button 'students' and select group."""
        super().setUpClass(first_admin, data['group_name'])

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def tearDown(self):
        super().tearDown()

    def test01_add_new_student_with_admin(self):
        """Check adding new student by administrator."""
        students_list_with_new_student = self.students_page.\
            click_edit_students_list_button().\
            click_add_new_student_button().\
            enter_student_data(data['first_new_student']).\
            click_save_data_changes_button().\
            click_exit_students_list_editor_button().\
            students_table()
        student = data_student_for_check(data['first_new_student'])
        self.assertEqual(self.main_page.get_current_url(),
                         data['expected_url'])
        self.assertIn(student, students_list_with_new_student)

    def test02_edit_data_first_student_with_admin(self):
        """Check is first student editing by administrator."""
        students_list_with_edit_student = self.students_page.\
            click_edit_students_list_button().\
            click_edit_student_button().\
            enter_student_data(data['first_new_data_student']).\
            click_save_data_changes_button().\
            click_exit_students_list_editor_button(). \
            students_table()
        student_with_changes = \
            data_student_for_check(data['first_new_data_student'])
        self.assertEqual(self.main_page.get_current_url(),
                         data['expected_url'])
        self.assertIn(student_with_changes,
                      students_list_with_edit_student)

    def test03_add_cv_first_student_with_admin(self):
        """Check is cv file added to the student's data
        by administrator."""
        actual_name_file = self.students_page.\
            click_edit_students_list_button().\
            click_add_new_student_button().\
            add_cv(data['path_file_cv']).\
            get_name_cv_file()
        self.assertEqual(actual_name_file,
                         data['expected_name_file_cv'])

    def test04_add_photo_first_student_with_admin(self):
        """Check is photo file added to the student's data
        by administrator."""
        actual_name_file = self.students_page.\
            click_edit_students_list_button().\
            click_add_new_student_button().\
            add_photo(data['path_file_photo']).\
            get_name_photo_file()
        self.assertEqual(actual_name_file,
                         data['expected_name_file_photo'])

    def test05_students_list_sort_by_name(self):
        """Check with role administrator is student's list sorting by name."""
        # get sorted list with function without None
        sorted_list_by_function = \
            remove_none_from_list(sorted(self.students_page.students_table()))
        # get sorted list with button without None
        sorted_list_by_button = \
            remove_none_from_list(self.students_page.
                                  click_students_list_sort_by_name_button().
                                  students_table())
        self.assertEqual(sorted_list_by_button, sorted_list_by_function)

    def test06_add_student_with_empty_fields(self):
        """Check adding new student with empty fields by administrator"""
        student_data = self.students_page.\
            click_edit_students_list_button(). \
            click_add_new_student_button()
        student_data.save_data_changes_button.click()
        actual_warnings = \
            student_data.warnings_text_for_adding_student_with_empty_fields()
        self.assertEqual(actual_warnings, data['expected_warnings'])

    def test07_remove_first_student_with_admin(self):
        """Check deleting first student from the student's list
        by administrator."""
        first_student = self.students_page.students_table()[0]
        students_list_without_first_student = self.students_page.\
            click_edit_students_list_button().\
            click_delete_first_student_button().\
            click_exit_students_list_editor_button().\
            students_table()
        self.assertEqual(self.main_page.get_current_url(),
                         data['expected_url'])
        self.assertNotIn(first_student,
                         students_list_without_first_student)

    def test08_add_equal_students_with_admin(self):
        """Check opportunity of adding two equal students by administrator."""
        actual_save_data_changes_button = \
            self.students_page.click_edit_students_list_button().\
            click_add_new_student_button().\
            enter_student_data(data['first_new_student']). \
            click_save_data_changes_button().\
            click_add_new_student_button(). \
            enter_student_data(data['first_new_student']). \
            save_data_changes_button
        actual_save_data_changes_button.click()
        # save data changes button have not to be enabled for
        # adding two equal students
        self.assertTrue(actual_save_data_changes_button.is_enabled())


class TestStudentsPageWithCoordinator(TestBaseSetUP):
    driver = None

    @classmethod
    def setUpClass(cls, user='', group=''):
        """Log in by coordinator, open top menu,select
        button 'students', select group."""
        super().setUpClass(coordinator, data['group_name'])

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def tearDown(self):
        super().tearDown()

    def test09_add_new_student_with_coordinator(self):
        """Check is new student added by coordinator."""
        students_list_with_new_student = self.students_page. \
            click_edit_students_list_button(). \
            click_add_new_student_button(). \
            enter_student_data(data['second_new_student']). \
            click_save_data_changes_button(). \
            click_exit_students_list_editor_button(). \
            students_table()
        student = data_student_for_check(data['second_new_student'])
        self.assertEqual(self.main_page.get_current_url(),
                         data['expected_url'])
        self.assertIn(student, students_list_with_new_student)

    def test10_edit_data_first_student_with_coordinator(self):
        """Check is first student editing by coordinator."""
        students_list_with_edit_student = self.students_page. \
            click_edit_students_list_button(). \
            click_edit_student_button(). \
            enter_student_data(data['second_new_data_student']). \
            click_save_data_changes_button(). \
            click_exit_students_list_editor_button(). \
            students_table()
        student_with_changes = \
            data_student_for_check(data['second_new_data_student'])
        self.assertEqual(self.main_page.get_current_url(),
                         data['expected_url'])
        self.assertIn(student_with_changes,
                      students_list_with_edit_student)

    def test11_add_cv_first_student_with_coordinator(self):
        """Check is cv file added to the student's data
        by coordinator."""
        actual_name_file = self.students_page. \
            click_edit_students_list_button(). \
            click_add_new_student_button(). \
            add_cv(data['path_file_cv']). \
            get_name_cv_file()
        self.assertEqual(actual_name_file, data['expected_name_file_cv'])

    def test12_add_photo_first_student_with_coordinator(self):
        """Check is photo file added to the student's data
        by coordinator."""
        actual_name_file = self.students_page. \
            click_edit_students_list_button(). \
            click_add_new_student_button(). \
            add_photo(data['path_file_photo']). \
            get_name_photo_file()
        self.assertEqual(actual_name_file, data['expected_name_file_photo'])

    def test13_remove_first_student_with_coordinator(self):
        """Check deleting first student from the student's list
        by coordinator."""
        first_student = self.students_page.students_table()[0]
        students_list_without_first_student = self.students_page. \
            click_edit_students_list_button(). \
            click_delete_first_student_button(). \
            click_exit_students_list_editor_button(). \
            students_table()
        self.assertEqual(self.main_page.get_current_url(),
                         data['expected_url'])
        self.assertNotIn(first_student,
                         students_list_without_first_student)


class TestStudentsPageWithTeacher(TestBaseSetUP):
    driver = None

    @classmethod
    def setUpClass(cls, user='', group=''):
        """Log in by teacher, open top menu,select
        button 'students', select group."""
        super().setUpClass(teacher, data['group_name'])

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def tearDown(self):
        super().tearDown()

    def test14_add_new_student_with_teacher(self):
        """Check is new student added by teacher."""
        students_list_with_new_student = self.students_page. \
            click_edit_students_list_button(). \
            click_add_new_student_button(). \
            enter_student_data(data['third_new_student']).\
            enter_name_approved_by_custom(data['third_new_student']). \
            click_save_data_changes_button(). \
            click_exit_students_list_editor_button(). \
            students_table()
        student = data_student_for_check(data['third_new_student'])
        self.assertEqual(self.main_page.get_current_url(),
                         data['expected_url'])
        self.assertIn(student, students_list_with_new_student)
        return self.students_page

    def test15_edit_data_first_student_with_teacher(self):
        """Check is first student editing by teacher."""
        students_list_with_edit_student = self.students_page. \
            click_edit_students_list_button(). \
            click_edit_student_button(). \
            enter_student_data(data['third_new_data_student']). \
            enter_name_approved_by_custom(data['third_new_data_student']). \
            click_save_data_changes_button(). \
            click_exit_students_list_editor_button(). \
            students_table()
        student_with_changes = \
            data_student_for_check(data['third_new_data_student'])
        self.assertEqual(self.main_page.get_current_url(),
                         data['expected_url'])
        self.assertIn(student_with_changes,
                      students_list_with_edit_student)
        return self.students_page

    def test16_add_cv_first_student_with_teacher(self):
        """Check is cv file added to the student's data
        by teacher."""
        actual_name_file = self.students_page. \
            click_edit_students_list_button(). \
            click_add_new_student_button(). \
            add_cv(data['path_file_cv']). \
            get_name_cv_file()
        self.assertEqual(actual_name_file,
                         data['expected_name_file_cv'])

    def test17_add_photo_first_student_with_teacher(self):
        """Check is photo file added to the student's data
        by teacher."""
        actual_name_file = self.students_page.\
            click_edit_students_list_button().\
            click_add_new_student_button(). \
            add_photo(data['path_file_photo']).\
            get_name_photo_file()
        self.assertEqual(actual_name_file,
                         data['expected_name_file_photo'])

    def test18_remove_first_student_with_teacher(self):
        """Check deleting first student from the student's list
        by teacher."""
        first_student = self.students_page.students_table()[0]
        students_list_without_first_student = self.students_page. \
            click_edit_students_list_button(). \
            click_delete_first_student_button(). \
            click_exit_students_list_editor_button(). \
            students_table()
        self.assertEqual(self.main_page.get_current_url(),
                         data['expected_url'])
        self.assertNotIn(first_student,
                         students_list_without_first_student)


class TestStudentsPageFromGroupWithAdmin(TestBase):

    def setUp(self):
        """Log in by administrator, select group."""
        super().setUp()
        self.login_page.auto_login(first_admin)
        self.main_page = GroupsPage(self.driver)
        self.main_page.select_group_by_name(data['group_name'])
        self.students_page = StudentsPage(self.driver)

    def tearDown(self):
        super().tearDown()

    def test19_opening_students_list_editor_after_selecting_group(self):
        """Check opportunity of opening student's list editor after
        selecting group and click on button 'students'."""
        self.students_page.click_students_from_group_button()
        self.students_page.click_edit_students_list_button()
        # test fail, because student's list editor does not open
        # after click on button "edit_students_list_button"
        self.assertTrue(self.students_page.
                        click_edit_students_list_button().
                        click_add_new_student_button().is_enabled())


if __name__ == '__main__':
    unittest.main()
