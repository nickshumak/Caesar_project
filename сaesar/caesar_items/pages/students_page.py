import os
from selenium.webdriver.support.ui import WebDriverWait
from caesar_items.pages.base_page import BasePage
from caesar_items.locators.locators import StudentsListLocators, \
    EditStudentsListLocators


class Student(object):

    def __init__(self, first_name, last_name, incoming_mark, entry_mark):
        self.first_name = first_name
        self.last_name = last_name
        self.incoming_mark = incoming_mark
        self.entry_mark = entry_mark


class StudentData(object):

    def __init__(self, driver):
        self.driver = driver

    def click_button_save_changes_data(self):
        WebDriverWait(self.driver, 20). \
            until(lambda driver: self.driver.
                  find_element(*EditStudentsListLocators.
                               BUTTON_SAVE_CHANGES)).click()
        return self

    def enter_student_first_name(self, student):
        self.driver.find_element(*EditStudentsListLocators.
                                 TEXT_FIELD_FIRST_NAME).clear()
        self.driver.find_element(*EditStudentsListLocators.
                                 TEXT_FIELD_FIRST_NAME). \
            send_keys(student.first_name)

    def enter_student_last_name(self, student):
        self.driver.find_element(*EditStudentsListLocators.
                                 TEXT_FIELD_LAST_NAME).clear()
        self.driver.find_element(*EditStudentsListLocators.
                                 TEXT_FIELD_LAST_NAME). \
            send_keys(student.last_name)

    def select_english_level(self):
        self.driver.find_element(*EditStudentsListLocators.
                                 LIST_ENGLISH_LEVEL).click()
        self.driver.find_element(*EditStudentsListLocators.
                                 PRE_INTERMEDIATE_LOW).click()

    def enter_student_mark_incoming_test(self, student):
        self.driver.find_element(*EditStudentsListLocators.
                                 STUDENT_MARK_INCOMING_TEST). \
            clear()
        self.driver.find_element(*EditStudentsListLocators.
                                 STUDENT_MARK_INCOMING_TEST). \
            send_keys(student.incoming_mark)

    def enter_student_entry_mark(self, student):
        self.driver.find_element(*EditStudentsListLocators.
                                 STUDENT_ENTRY_SCORE).clear()
        self.driver.find_element(*EditStudentsListLocators.
                                 STUDENT_ENTRY_SCORE). \
            send_keys(student.entry_mark)

    def select_who_approved(self):
        self.driver.find_element(*EditStudentsListLocators.
                                 STUDENT_APPROVED_BY).click()
        self.driver.find_element(*EditStudentsListLocators.
                                 APPROVED_BY).click()

    def enter_student_data(self, student):
        self.enter_student_first_name(student)
        self.enter_student_last_name(student)
        self.select_english_level()
        self.enter_student_mark_incoming_test(student)
        self.enter_student_entry_mark(student)
        self.select_who_approved()

    def add_cv(self, path_file_cv):
        self.driver.find_element(*EditStudentsListLocators.
                                 BUTTON_ADDING_CV).click()
        self.driver.find_element(*EditStudentsListLocators.
                                 INPUT_ADDING_CV).\
            send_keys(os.path.abspath(path_file_cv))

    def get_name_cv_file(self):
        return self.driver.find_element(*EditStudentsListLocators.
                                        FILE_NAME_CV).text

    def add_photo(self, path_file_photo):
        self.driver.find_element(*EditStudentsListLocators.
                                 BUTTON_ADDING_PHOTO).click()
        self.driver.find_element(*EditStudentsListLocators.
                                 INPUT_ADDING_PHOTO).\
            send_keys(os.path.abspath(path_file_photo))

    def get_name_photo_file(self):
        return self.driver.find_elements(*EditStudentsListLocators.
                                         FILE_NAME_PHOTO)[-1].text


class StudentsList(object):

    def __init__(self, driver):
        self.driver = driver
        self.student_data = StudentData(self.driver)

    def click_button_delete_first_student(self):
        self.driver.find_element(*EditStudentsListLocators.
                                 BUTTON_DELETE_STUDENT).click()
        WebDriverWait(self.driver, 20). \
            until(lambda driver: self.driver.
                  find_element(*EditStudentsListLocators.
                               BUTTON_CONFIRM_DELETING)).click()
        return self

    def click_button_add_new_student(self):
        self.driver.find_element(*EditStudentsListLocators.
                                 BUTTON_ADD_NEW_STUDENT).click()
        return self

    def click_button_edit_student(self):
        self.driver.find_element(*EditStudentsListLocators.
                                 BUTTON_EDIT_STUDENT).click()
        return self

    def click_button_exit_editor_students_list(self):
        return self.driver.find_element(*EditStudentsListLocators.
                                        BUTTON_EXIT_EDIT_STUDENTS_LIST). \
            click()


class StudentsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.students_list = StudentsList(self.driver)

    def students_table(self):
        students_data = []
        list_rows = \
            self.driver.find_elements(*StudentsListLocators.
                                      STUDENTS_LISTS_ROWS)
        for column in list_rows:
            students_data.append(column.text)
        return students_data

    def click_button_edit_students_list(self):
        self.driver.find_element(*StudentsListLocators.
                                 BUTTON_EDIT_STUDENTS_LIST).click()
        return self

    def get_current_url(self):
        return self.driver.get_url()


def data_student_for_check(student):
    data_student = [student.last_name, student.first_name,
                    'Pre-intermediate low', student.incoming_mark,
                    student.entry_mark, 'N. Varenko']
    data_student = ' '.join(data_student)
    return data_student
