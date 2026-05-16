from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 30)

    # ================= LOCATORS =================

    first_name = (By.ID, "first-name")

    last_name = (By.ID, "last-name")

    postal_code = (By.ID, "postal-code")

    continue_btn = (By.ID, "continue")

    finish_btn = (By.ID, "finish")

    success_message = (
        By.CLASS_NAME,
        "complete-header"
    )

    # ================= ACTIONS =================

    def enter_checkout_details(
        self,
        fname,
        lname,
        zipcode
    ):

        self.wait.until(
            EC.visibility_of_element_located(
                self.first_name
            )
        ).send_keys(fname)

        self.driver.find_element(
            *self.last_name
        ).send_keys(lname)

        self.driver.find_element(
            *self.postal_code
        ).send_keys(zipcode)

    def click_continue(self):

        continue_button = self.wait.until(
            EC.presence_of_element_located(
                self.continue_btn
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            continue_button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            continue_button
        )

        # Wait for checkout overview page
        self.wait.until(
            EC.visibility_of_element_located(
                self.finish_btn
            )
        )

    def click_finish(self):

        finish_button = self.wait.until(
            EC.presence_of_element_located(
                self.finish_btn
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            finish_button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            finish_button
        )

    def get_success_message(self):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.success_message
            )
        )

        return element.text