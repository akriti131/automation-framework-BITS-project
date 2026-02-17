import pytest
from utils.driver_factory import DriverFactory
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader

@pytest.fixture
def driver():
    driver = DriverFactory().get_driver()
    yield driver
    driver.quit()

def test_valid_login(driver):
    config = ConfigReader()
    login_page = LoginPage(driver)

    login_page.login(config.get_username(), config.get_password())

    assert "Swag Labs" in driver.title
    # assert "InvalidText" in driver.title    ---- use this to test failure


