from selenium import webdriver
from resource.url_site import PathUrl
from resource.path_driver import GetDriver


class BasePage(object):

    driver = webdriver.Chrome(
        executable_path=GetDriver.DRIVER_CHROME)
    driver.get(PathUrl.URL_SITE)
    driver.maximize_window()

    def get_title_name(self):
        return self.driver.title

    def get_page(self, request):
        self.driver.get(request)
        return self

    def get_current_url(self):
        return self.driver.current_url

    def quit(self):
        self.driver.quit()
