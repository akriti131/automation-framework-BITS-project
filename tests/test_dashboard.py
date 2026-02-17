import pytest
from utils.driver_factory import DriverFactory
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config_reader import ConfigReader

@pytest.fixture
def driver():
    driver = DriverFactory().get_driver()
    yield driver
    driver.quit()

def test_dashboard_loaded(driver):
    config = ConfigReader()
    login_page = LoginPage(driver)
    dashboard = DashboardPage(driver)

    login_page.login(config.get_username(), config.get_password())

    assert dashboard.get_page_title() == "Products"

