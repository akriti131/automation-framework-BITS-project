from selenium.webdriver.common.by import By

from utils.logger import Logger

logger = Logger.get_logger()
logger.info("Entering username")
logger.info("Clicking login button")


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    error_message = (By.CSS_SELECTOR, "[data-test='error']")

    def is_error_displayed(self):
        return len(self.driver.find_elements(*self.error_message)) > 0
