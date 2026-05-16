from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 30)

    # ================= LOCATORS =================

    product_name = (
        By.CLASS_NAME,
        "inventory_item_name"
    )

    checkout_btn = (
        By.ID,
        "checkout"
    )

    # ================= ACTIONS =================

    def get_product_name(self):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.product_name
            )
        )

        return element.text

    def click_checkout(self):

        # Wait for button presence
        checkout_button = self.wait.until(
            EC.presence_of_element_located(
                self.checkout_btn
            )
        )

        # Scroll to element
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            checkout_button
        )

        # JS Click (Most stable for CI/headless)
        self.driver.execute_script(
            "arguments[0].click();",
            checkout_button
        )

        # Wait for checkout page
        self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "first-name")
            )
        )