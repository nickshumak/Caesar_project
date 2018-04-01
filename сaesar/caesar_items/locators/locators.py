from selenium.webdriver.common.by import By


class LogInLocators(object):
    LOGIN_FIELD = (By.NAME, 'login')
    PASSWORD_FIELD = (By.NAME, 'password')
    CONFIRM_ACTION = (By.CLASS_NAME, 'submit')
    FIELD_MESSAGE = (By.CLASS_NAME, 'message')


class GroupPageLocators(object):
    GROUP_LOCATION = (By.CLASS_NAME, 'groupLocation')
    BUTTON_SEARCH = (By.CSS_SELECTOR, 'div.search')

    # GROUPS = (By.CLASS_NAME, 'group-collection row')

    BUTTON_MY_GROUPS = (By.CLASS_NAME, 'myGroups')
    BUTTON_ALL_GROUPS = (By.CLASS_NAME, 'allGroups')
    BUTTONS_STAGE_GROUPS = (By.CLASS_NAME, 'stage-toggle')

    # надо определиться как делаем, так не красиво или через массив?селекторы проверила
    ENDED_GROUPS = (By.CSS_SELECTOR, '.stage-toggle > label:nth-child(2)')
    CURRENT_GROUPS = (By.CSS_SELECTOR, '.stage-toggle > label:nth-child(4)')
    BOARDING_GROUPS = (By.CSS_SELECTOR, '.stage-toggle > label:nth-child(6)')

    GROUPS = (By.CLASS_NAME, 'small-group-view')

    # main section
    GROUP_NAME = (By.CLASS_NAME, 'content-header-group-name')
    BUTTON_EDIT_GROUP = (By.NAME, 'edit')
    BUTTON_INFO_GROUP = (By.NAME, 'info')
    BUTTON_STUDENTS_IN_GROUP = (By.NAME, 'students')
    BUTTON_SCHEDULE_GROUP = (By.NAME, 'shedule')
    BUTTON_MESSAGE_GROUP = (By.NAME, 'message')

    GROUP_COORDINATION = (By.CLASS_NAME, 'group_coordination')
    GROUP_INFO = (By.CLASS_NAME, 'group_info')
    KEY_DATES = (By.CLASS_NAME, 'key - dates')
    GROUP_STAGE_TITLE = (By.CLASS_NAME, 'groupStageTitle')
    GROUP_STAGE = (By.CLASS_NAME, 'groupStage')

    LEFT_MENU = (By.CSS_SELECTOR, '#left-menu > div')
    USER_PHOTO = (By.CLASS_NAME, 'user-photo')
    TOP_MENU = (By.CLASS_NAME, 'row')
    BUTTON_CONFIRM_DELETION = (By.CLASS_NAME, 'fa fa-check-circle-o fa-3x')
    BUTTON_CANCEL_DELETION = (By.CLASS_NAME, 'fa fa-times-circle-o fa-3x')


class RightMenuLocators(object):
    BUTTON_EDIT_PROFILE = (By.CLASS_NAME, 'btn-edit')
    USER_NAME = (By.CLASS_NAME, 'name')
    USER_ROLE = (By.CLASS_NAME, 'role')
    BUTTON_LOGOUT = (By.CSS_SELECTOR, 'a.logout:nth-child(3)')


class LeftMenuLocators(object):
    BUTTON_CREATE_GROUP = (By.XPATH, '//*[@title = "Create"]')
    BUTTON_SEARCH_GROUP = (By.XPATH, '//*[@title = "Search"]')
    BUTTON_EDIT_GROUP = (By.XPATH, '//*[@title = "Edit"]')
    BUTTON_DELETE_GROUP = (By.XPATH, '//*[@title = "Delete"]')


class TopMenuLocators(object):
    BUTTON_LOCATIONS = (By.CSS_SELECTOR, 'div.itemMenu:nth-child(1)')
    BUTTON_GROUPS = (By.CSS_SELECTOR, 'div.itemMenu:nth-child(2)')
    BUTTON_STUDENTS = (By.CSS_SELECTOR, 'div.itemMenu:nth-child(3)')
    BUTTON_SCHEDULE = (By.CSS_SELECTOR, 'div.itemMenu:nth-child(4)')
    BUTTON_ADD = (By.CSS_SELECTOR, 'div.itemMenu:nth-child(5)')
    BUTTON_ABOUT = (By.CSS_SELECTOR, 'div.itemMenu:nth-child(6)')

    BUTTON_LOGOUT = (By.CLASS_NAME, 'logout')


class AdminPageLocators(object):
    ADD_USER = (By.XPATH, ".//*[text()='Add user']")
    ADD_GROUP = (By.XPATH, "/.//*[text()='Add group']")
    ADD_STUDENT = (By.XPATH, ".//*[text()='Add student']")
    TAB_USERS = (By.CSS_SELECTOR, "a[href*='users']")
    TAB_GROUPS = (By.CSS_SELECTOR, "a[href*='groups']")
    TAB_STUDENTS = (By.CSS_SELECTOR, "a[href*='students']")
    BUTTON_ESCAPE = (By.CSS_SELECTOR, '.btn.btn-warning.home')
    TITLE_ENTITY = (By.CSS_SELECTOR, '.modal-title')
    BUTTON_SUBMIT = (By.CSS_SELECTOR, ".btn.btn-primary.submit")

    @staticmethod
    def get_request_table(table):
        table = ".//*[@id='{type}']/div/table/tbody//td[position()<last()]" \
            .format(type=table)
        return table


class CreateEditUsersLocators(object):
    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")
    ROLE = (By.NAME, "role")
    LOCATION = (By.NAME, "location")
    PHOTO = (By.NAME, "photo")
    LOGIN_FIELD = (By.NAME, "login")
    PASSWORD_FIELD = (By.NAME, "password")
    DELETE_BUTTONS = "(//tbody//button[@class='btn btn-danger delete'])"


class CreateEditGroupsLocators(object):
    NAME = (By.NAME, "name")
    LOCATION = (By.NAME, "location")
    DIRECTION = (By.NAME, "direction")
    START_DATE = (By.NAME, "startDate")
    FINISH_DATE = (By.NAME, "finishDate")
    TEACHERS = (By.NAME, "teachers")
    EXPERTS = (By.NAME, "experts")
    STAGE = (By.NAME, "stage")
    BUDGET = (By.NAME, "budgetOwner")


class CreateEditStudentsLocators(object):
    GROUP_ID = (By.NAME, 'groupID')
    NAME = (By.NAME, "name")
    LAST_NAME = (By.NAME, "lastName")
    ENGLISH_LEVEL = (By.NAME, "englishLevel")
    CV_URL = (By.NAME, "CvUrl")
    IMAGE = (By.NAME, "imageUrl")
    ENTRY_SCORE = (By.NAME, "entryScore")
    APPROVED_BY = (By.NAME, 'approvedBy')


class CreateGroupWindowLocators(object):
    GROUP_NAME_FORM = (
        By.CSS_SELECTOR, '#modal-window > section > section > section > '
                         'div:nth-child(1) > div:nth-child(1) > div > div')
    FIELD_GROUP_NAME = (By.NAME, 'name')
    FORM_DIRECTION = (
        By.CSS_SELECTOR, '#modal-window > section > section > section > '
                         'div:nth-child(3) > div:nth-child(1)')
    DROP_LIST_DIRECTION = (By.NAME, 'direction')
    DROP_LIST_LOCATION = (By.NAME, 'location')
    BUTTON_ONE_MORE_TEACHER = (By.CLASS_NAME, 'add-teacher-btn')
    DROP_LIST_TEACHERS = (By.NAME, 'teacher')
    BUTTON_ACCEPT_TEACHER = (By.ID, 'acceptSelect')
    FORM_ADDED_TEACHERS = (By.CLASS_NAME, 'list-item')
    BUTTON_BUDGET_OWNER_SOFT_SERVE = (By.CLASS_NAME,
                                      'btn btn-default budget-option')
    # BUTTON_BUDGET_OWNER_OPEN_GROUP=
    FORM_START_DATE = (
        By.CSS_SELECTOR, '#modal-window > section > section > section > '
                         'div:nth-child(3) > '
                         'div.form-group.col-xs-6.col-xs-offset-0.col-md-5.'
                         'col-md-offset-1.col-lg-4.calendar-wrapper')
    DATE_START = (By.NAME, 'startDate')
    DATE_FINISH = (By.NAME, 'finishDate')
    BUTTON_ADD_EXPERT = (By.CLASS_NAME, 'add-expert-btn')
    FIELD_EXPERTS_NAME = (By.NAME, 'expert')
    BUTTON_ACCEPT_EXPERT = (By.ID, 'acceptInput')
    SAVE_BUTTON = (By.ID, 'save')
    CANCEL_BUTTON = (By.ID, 'cancel')


# for students
class StudentsListLocators(object):
    BUTTON_EDIT_STUDENTS_LIST = \
        (By.XPATH, './/*[@id="main-section"]/div/header/div[1]/button')
    BUTTON_STUDENTS_IN_STUDENTS_LIST = (By.CLASS_NAME, 'students')
    BUTTON_SCHEDULE_IN_STUDENTS = (By.CLASS_NAME, 'shedule')
    BUTTON_MESSAGE_IN_STUDENTS = (By.CLASS_NAME, 'message')
    STUDENTS_LISTS_ROWS = (By.CLASS_NAME, 'tableBodyStudents')


class EditStudentsListLocators(object):
    NAME_STUDENT_LIST = \
        (By.CSS_SELECTOR, '.header-modal-editStudentlist > span:nth-child(1)')
    STUDENTS_TABLE = (By.CLASS_NAME, 'tableBodyStudents')
    BUTTON_EXIT_EDIT_STUDENTS_LIST = (By.CLASS_NAME, 'exit')
    BUTTON_DELETE_STUDENT = (By.XPATH, './/*[@id="modal-window"]//td[6]/i')
    BUTTON_CONFIRM_DELETING = (By.XPATH, './/*[@id="modal-window"]//button[1]')
    BUTTON_ADD_NEW_STUDENT = \
        (By.XPATH, './/*[@id="modal-window"]/section//button[1]')
    BUTTON_EDIT_STUDENT = (By.XPATH, './/*[@id="modal-window"]/section//td[5]/i')

    # fields for student
    TEXT_FIELD_FIRST_NAME = \
        (By.XPATH, './/*[@id="modal-window"]/div/section/section/div[2]/div[1]/input')
    TEXT_FIELD_LAST_NAME = \
        (By.XPATH, './/*[@id="modal-window"]/div/section/section/div[3]/div[1]/input')
    LIST_ENGLISH_LEVEL = \
        (By.XPATH, './/*[@id="modal-window"]/div/section/section/div[4]/div[1]/select')
    PRE_INTERMEDIATE_LOW = \
        (By.XPATH, './/*[@id = "modal-window"]/div/section/section/div[4]/div[1]/select/option[2]')
    STUDENT_MARK_INCOMING_TEST = \
        (By.XPATH, './/*[@id="modal-window"]/div/section/section/div[1]/div[2]/input')
    STUDENT_ENTRY_SCORE = \
        (By.XPATH, './/*[@id="modal-window"]/div/section/section/div[2]/div[2]/input')
    STUDENT_APPROVED_BY = \
        (By.XPATH, './/*[@id="modal-window"]/div/section/section/div[3]/div[2]/select')
    APPROVED_BY = (By.XPATH, './/*[@id="modal-window"]/div/section/section/div[3]/div[2]/select/option[2]')
    BUTTON_SAVE_CHANGES = \
        (By.XPATH, './/*[@id="modal-window"]/div/section/section/div[6]/button[1]')
    BUTTON_ADDING_CV = \
        (By.XPATH, './/*[@id="modal-window"]/div/section/section/div[5]/div[1]/button')
    INPUT_ADDING_CV = \
        (By.XPATH, './/*[@id="modal-window"]/div/section/section/div[5]/div[1]/input')
    FILE_NAME_CV = (By.CLASS_NAME, 'list-item')
    BUTTON_ADDING_PHOTO = \
        (By.XPATH, './/*[@id="modal-window"]/div/section/section/div[5]/div[2]/button')
    INPUT_ADDING_PHOTO = \
        (By.XPATH, './/*[@id="modal-window"]/div/section/section/div[5]/div[2]/input')
    FILE_NAME_PHOTO = \
        (By.XPATH, './/*[@id="modal-window"]/div/section/section/div[5]/div[2]/ul/li/span[1]')
