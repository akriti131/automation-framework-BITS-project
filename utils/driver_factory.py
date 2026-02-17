from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from utils.config_reader import ConfigReader
from utils.logger import Logger
import os

class DriverFactory:

    def get_driver(self):
        config = ConfigReader()
        browser = config.get_browser()
        headless = config.is_headless()

        logger = Logger.get_logger()
        logger.info("Initializing WebDriver")

        if browser.lower() == "chrome":

            driver_path = os.path.join("drivers", "chromedriver.exe")
            logger.info(f"Using local driver: {driver_path}")

            options = Options()

            if headless:
                logger.info("Running in HEADLESS mode")
                options.add_argument("--headless=new")

            options.add_argument("--start-maximized")

            service = Service(driver_path)
            driver = webdriver.Chrome(service=service, options=options)

            driver.implicitly_wait(config.get_implicit_wait())
            driver.get(config.get_base_url())

            logger.info(f"Opened URL: {config.get_base_url()}")

            return driver
