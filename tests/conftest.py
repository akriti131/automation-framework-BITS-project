import os
import pytest
from datetime import datetime
from utils.driver_factory import DriverFactory


# ✅ DRIVER FIXTURE
@pytest.fixture
def driver():
    driver = DriverFactory().get_driver()
    yield driver
    driver.quit()


# ✅ SCREENSHOT ON FAILURE HOOK
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = "reports/screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join(screenshots_dir, file_name)

            driver.save_screenshot(file_path)
            print(f"\n📸 Screenshot captured: {file_path}")