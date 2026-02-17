from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.config_reader import ConfigReader
from utils.logger import Logger
import os


class DriverFactory:

    def get_driver(self):
        config = ConfigReader()
        browser = config.get_browser()

        logger = Logger.get_logger()
        logger.info("Initializing WebDriver")

        if browser.lower() == "chrome":
            driver_path = os.path.join("drivers", "chromedriver.exe")

            if not os.path.exists(driver_path):
                logger.error(f"ChromeDriver not found at: {driver_path}")
                raise FileNotFoundError(f"ChromeDriver not found at: {driver_path}")

            logger.info(f"Using driver: {driver_path}")

            service = Service(driver_path)
            driver = webdriver.Chrome(service=service)

            driver.maximize_window()
            driver.implicitly_wait(config.get_implicit_wait())

            driver.get(config.get_base_url())
            logger.info(f"Opened URL: {config.get_base_url()}")

            return driver
