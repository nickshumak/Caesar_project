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
    FUTURE_GROUPS = (By.CSS_SELECTOR, '.stage-toggle > label:nth-child(6)')

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


class WindowCreateGroup(object):
    FORM_GROUP_NAME = (
        By.CSS_SELECTOR, '#modal-window > section > section > section > '
                         'div:nth-child(1) > div:nth-child(1) > div > div')
    FIELD_GROUP_NAME = (By.NAME, 'name')
    DROP_LIST_DIRECTION = (By.NAME, 'direction')
    DROP_LIST_LOCATION = (By.NAME, 'location')
    BUTTON_TEACHERS_ADD = (By.CLASS_NAME, 'add-teacher-btn')
    DROP_LIST_TEACHERS = (By.NAME, 'teacher')
    BUTTON_ACCEPT_TEACHER = (By.ID, 'acceptSelect')
    BUTTON_BUDGET_OWNER_SOFT_SERVE = (By.CLASS_NAME,
                                      'btn btn-default budget-option')
    # BUTTON_BUDGET_OWNER_OPEN_GROUP=
    DATE_START = (By.NAME, 'startDate')
    DATE_FINISH = (By.NAME, 'finishDate')
    BUTTON_ADD_EXPERT = (By.CLASS_NAME, 'add-expert-btn')
    FIELD_EXPERTS_NAME = (By.NAME, 'expert')
    BUTTON_ACCEPT_EXPERT = (By.ID, 'acceptInput')
    BUTTON_SAVE = (By.ID, 'save')
