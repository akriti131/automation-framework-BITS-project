from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # Locators
    product_name = (By.CLASS_NAME, "inventory_item_name")

    checkout_btn = (By.ID, "checkout")

    # Actions
    def get_product_name(self):

        element = self.wait.until(
            EC.visibility_of_element_located(self.product_name)
        )

        return element.text

    def click_checkout(self):

        self.wait.until(
            EC.element_to_be_clickable(self.checkout_btn)
        ).click()