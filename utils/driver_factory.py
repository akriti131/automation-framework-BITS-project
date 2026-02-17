import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from utils.config_reader import ConfigReader
from utils.logger import Logger

class DriverFactory:

    def get_driver(self):
        config = ConfigReader()
        browser = config.get_browser()
        logger = Logger.get_logger()

        logger.info("Initializing WebDriver")

        options = Options()

        # ✅ Headless for CI
        if os.getenv("CI") == "true":
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            logger.info("Running in CI → Headless mode enabled")

        if browser.lower() == "chrome":

            # ✅ Use webdriver-manager in CI
            if os.getenv("CI") == "true":
                logger.info("Using webdriver-manager for CI")
                service = Service(ChromeDriverManager().install())

            else:
                driver_path = os.path.join("drivers", "chromedriver.exe")
                logger.info(f"Using local driver: {driver_path}")
                service = Service(driver_path)

            driver = webdriver.Chrome(service=service, options=options)

            driver.maximize_window()
            driver.implicitly_wait(config.get_implicit_wait())
            driver.get(config.get_base_url())

            logger.info(f"Opened URL: {config.get_base_url()}")

            return driver
