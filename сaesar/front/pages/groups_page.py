from front.pages.base_page import BasePage


class GroupsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    class LeftBar(object):
        """inner classes"""
        pass

    class RightBar(object):
        pass

    class HeadBar(object):
        pass
