# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from utils.config_reader import ConfigReader
# from utils.logger import Logger

# class DriverFactory:

#     def get_driver(self):
#         config = ConfigReader()
#         browser = config.get_browser()
#         logger = Logger.get_logger()

#         logger.info("Initializing WebDriver")

#         options = Options()

#         # ✅ Headless for CI
#         if os.getenv("CI") == "true":
#             options.add_argument("--headless=new")
#             options.add_argument("--no-sandbox")
#             options.add_argument("--disable-dev-shm-usage")
#             logger.info("Running in CI → Headless mode enabled")

#         if browser.lower() == "chrome":

#             # ✅ Use webdriver-manager in CI
#             if os.getenv("CI") == "true":
#                 logger.info("Using webdriver-manager for CI")
#                 service = Service(ChromeDriverManager().install())

#             else:
#                 driver_path = os.path.join("drivers", "chromedriver.exe")
#                 logger.info(f"Using local driver: {driver_path}")
#                 service = Service(driver_path)

#             driver = webdriver.Chrome(service=service, options=options)

#             driver.maximize_window()
#             driver.implicitly_wait(config.get_implicit_wait())
#             driver.get(config.get_base_url())

#             logger.info(f"Opened URL: {config.get_base_url()}")

#             return driver







import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utils.config_reader import ConfigReader
from utils.logger import Logger


class DriverFactory:

    def get_driver(self):
        config = ConfigReader()
        browser = config.get_browser().lower()
        headless = config.is_headless()
        is_ci = os.getenv("CI") == "true"

        logger = Logger.get_logger()
        logger.info(f"Initializing WebDriver for: {browser}")

        driver = None

        # ================= CHROME =================
        if browser == "chrome":
            options = ChromeOptions()

            if headless or is_ci:
                options.add_argument("--headless=new")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                logger.info("Headless mode enabled")

            if is_ci:
                logger.info("CI detected → Using webdriver-manager")
                service = ChromeService(ChromeDriverManager().install())
            else:
                driver_path = os.path.join("drivers", "chromedriver.exe")
                logger.info(f"Using local Chrome driver: {driver_path}")
                service = ChromeService(driver_path)

            driver = webdriver.Chrome(service=service, options=options)

        # ================= EDGE =================
        elif browser == "edge":
            options = EdgeOptions()

            if headless or is_ci:
                options.add_argument("--headless=new")
                logger.info("Headless mode enabled")

            if is_ci:
                logger.info("CI detected → Using webdriver-manager")
                service = EdgeService(EdgeChromiumDriverManager().install())
            else:
                driver_path = os.path.join("drivers", "msedgedriver.exe")
                logger.info(f"Using local Edge driver: {driver_path}")
                service = EdgeService(driver_path)

            driver = webdriver.Edge(service=service, options=options)

        # ================= FIREFOX =================
        elif browser == "firefox":
            options = FirefoxOptions()

            if headless or is_ci:
                options.add_argument("--headless")
                logger.info("Headless mode enabled")

            if is_ci:
                logger.info("CI detected → Using webdriver-manager")
                service = FirefoxService(GeckoDriverManager().install())
            else:
                driver_path = os.path.join("drivers", "geckodriver.exe")
                logger.info(f"Using local Firefox driver: {driver_path}")
                service = FirefoxService(driver_path)

            driver = webdriver.Firefox(service=service, options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        # ================= COMMON SETUP =================
        driver.maximize_window()
        driver.implicitly_wait(config.get_implicit_wait())
        driver.get(config.get_base_url())

        logger.info(f"Opened URL: {config.get_base_url()}")

        return driver