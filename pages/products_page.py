from selenium.webdriver.common.by import By


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    add_backpack_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
    add_bike_light_btn = (By.ID, "add-to-cart-sauce-labs-bike-light")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    # Actions
    def add_backpack_to_cart(self):
        self.driver.find_element(*self.add_backpack_btn).click()

    def add_bike_light_to_cart(self):
        self.driver.find_element(*self.add_bike_light_btn).click()

    def open_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def get_cart_count(self):
        return self.driver.find_element(*self.cart_badge).text