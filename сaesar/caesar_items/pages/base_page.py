class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def get_title_name(self):
        return self.driver.title

    def get_page(self, request):
        self.driver.get(request)
        return self