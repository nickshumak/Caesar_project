"""
Tests check the additional, removal and editing of
 student data in the list of students
"""

from tests.test_base import TestBase
from front.pages.students_page import Student, data_student_for_check
from front.user import first_admin, teacher, coordinator
import unittest

expected_url = 'http://localhost:3000/Students/Dnipro/DP-093-JS/list'
# data for adding new student
new_student = Student(first_name='Vladyslava', last_name='Semmi',
                      incoming_mark='111', entry_mark='5')
second_new_student = Student('Sherlock', 'Holmes', '333', '3')
third_new_student = Student('Merlin', 'Monro', '123', '3')
# data for editing student
new_data_student = Student('Garry', 'Potter', '222', '2')
second_new_data_student = Student('Robin', 'Good', '444', '4')
third_new_data_student = Student('Clark', 'Kent', '321', '3')


class TestStudentsPage(TestBase):

    def test_add_new_student_with_admin(self):
        self.login_page.log_in_visitor(first_admin)
        self.students_page.students_list()
        self.students_page.click_button_edit_students_list()
        self.students_page.add_new_student(new_student)
        self.students_page.click_button_exit_editor_students_list()
        student = data_student_for_check(new_student)
        students_list = self.students_page.students_table()
        self.assertEqual(self.students_page.get_current_url(), expected_url)
        self.assertIn(student, students_list)

    def test_delete_first_student_with_admin(self):
        self.login_page.log_in_visitor(first_admin)
        self.students_page.students_list()
        first_student = self.students_page.students_table()[0]
        self.students_page.click_button_edit_students_list()
        self.students_page.click_button_delete_first_student()
        self.students_page.click_button_exit_editor_students_list()
        students_list = self.students_page.students_table()
        self.assertEqual(self.students_page.get_current_url(), expected_url)
        self.assertNotIn(first_student, students_list)

    def test_edit_data_first_student_with_admin(self):
        self.login_page.log_in_visitor(first_admin)
        self.students_page.students_list()
        self.students_page.click_button_edit_students_list()
        self.students_page.edit_student(new_data_student)
        self.students_page.click_button_exit_editor_students_list()
        student_with_changes = data_student_for_check(new_data_student)
        students_list = self.students_page.students_table()
        self.assertEqual(self.students_page.get_current_url(), expected_url)
        self.assertIn(student_with_changes, students_list)

    def test_add_new_student_with_coordinator(self):
        self.login_page.log_in_visitor(coordinator)
        self.students_page.students_list()
        self.students_page.click_button_edit_students_list()
        self.students_page.add_new_student(second_new_student)
        self.students_page.click_button_exit_editor_students_list()
        student = data_student_for_check(second_new_student)
        students_list = self.students_page.students_table()
        self.assertEqual(self.students_page.get_current_url(), expected_url)
        self.assertIn(student, students_list)

    def test_delete_first_student_with_coordinator(self):
        self.login_page.log_in_visitor(coordinator)
        self.students_page.students_list()
        first_student = self.students_page.students_table()[0]
        self.students_page.click_button_edit_students_list()
        self.students_page.click_button_delete_first_student()
        self.students_page.click_button_exit_editor_students_list()
        students_list = self.students_page.students_table()
        self.assertEqual(self.students_page.get_current_url(), expected_url)
        self.assertNotIn(first_student, students_list)

    def test_edit_data_first_student_with_coordinator(self):
        self.login_page.log_in_visitor(coordinator)
        self.students_page.students_list()
        self.students_page.click_button_edit_students_list()
        self.students_page.edit_student(second_new_data_student)
        self.students_page.click_button_exit_editor_students_list()
        student_with_changes = data_student_for_check(second_new_data_student)
        students_list = self.students_page.students_table()
        self.assertEqual(self.students_page.get_current_url(), expected_url)
        self.assertIn(student_with_changes, students_list)

    def test_add_new_student_with_teacher(self):
        self.login_page.log_in_visitor(teacher)
        self.students_page.students_list()
        self.students_page.click_button_edit_students_list()
        self.students_page.add_new_student(third_new_student)
        self.students_page.click_button_exit_editor_students_list()
        student = data_student_for_check(third_new_student)
        students_list = self.students_page.students_table()
        self.assertEqual(self.students_page.get_current_url(), expected_url)
        self.assertIn(student, students_list)

    def test_delete_first_student_with_teacher(self):
        self.login_page.log_in_visitor(teacher)
        self.students_page.students_list()
        first_student = self.students_page.students_table()[0]
        self.students_page.click_button_edit_students_list()
        self.students_page.click_button_delete_first_student()
        self.students_page.click_button_exit_editor_students_list()
        students_list = self.students_page.students_table()
        self.assertEqual(self.students_page.get_current_url(), expected_url)
        self.assertNotIn(first_student, students_list)

    def test_edit_data_first_student_with_teacher(self):
        self.login_page.log_in_visitor(teacher)
        self.students_page.students_list()
        self.students_page.click_button_edit_students_list()
        self.students_page.edit_student(third_new_data_student)
        self.students_page.click_button_exit_editor_students_list()
        student_with_changes = data_student_for_check(third_new_data_student)
        students_list = self.students_page.students_table()
        self.assertEqual(self.students_page.get_current_url(), expected_url)
        self.assertIn(student_with_changes, students_list)


if __name__ == '__main__':
    unittest.main()