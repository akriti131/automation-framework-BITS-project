from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    checkout_btn = (By.ID, "checkout")
    inventory_item = (By.CLASS_NAME, "inventory_item_name")

    # Actions
    def get_product_name(self):
        return self.driver.find_element(*self.inventory_item).text

    def click_checkout(self):
        self.driver.find_element(*self.checkout_btn).click()