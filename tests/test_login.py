# import pytest
# from utils.driver_factory import DriverFactory
# from pages.login_page import LoginPage
# from utils.config_reader import ConfigReader

# @pytest.fixture
# def driver():
#     driver = DriverFactory().get_driver()
#     yield driver
#     driver.quit()

# def test_valid_login(driver):
#     config = ConfigReader()
#     login_page = LoginPage(driver)

#     login_page.login(config.get_username(), config.get_password())

#     assert "Swag Labs" in driver.title
#     # assert "InvalidText" in driver.title    ---- use this to test failure


import pytest
from pages.login_page import LoginPage
from utils.data_reader import DataReader


test_data = DataReader.load_yaml("login_data.yaml")


@pytest.mark.parametrize("scenario", test_data.keys())
def test_login_scenarios(driver, scenario):

    data = test_data[scenario]

    login_page = LoginPage(driver)
    login_page.login(data["username"], data["password"])

    if data["expected"] == "success":
        assert "inventory" in driver.current_url
    else:
        assert login_page.is_error_displayed()