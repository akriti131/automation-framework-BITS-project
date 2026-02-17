from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    title = (By.CLASS_NAME, "title")

    def get_page_title(self):
        return self.driver.find_element(*self.title).text
