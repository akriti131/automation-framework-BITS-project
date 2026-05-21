import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.driver_factory import DriverFactory


@pytest.fixture
def driver():
    driver = DriverFactory().get_driver()
    yield driver
    driver.quit()


def test_checkout_flow(driver):

    # Login
    login_page = LoginPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    # Add Product
    products_page = ProductsPage(driver)

    products_page.add_backpack_to_cart()

    products_page.open_cart()

    # Cart Page
    cart_page = CartPage(driver)

    cart_page.click_checkout()

    # Checkout Page
    checkout_page = CheckoutPage(driver)

    checkout_page.enter_checkout_details(
        "Akriti",
        "Singh",
        "400001"
    )

    checkout_page.click_continue()

    checkout_page.click_finish()

    # Validate success message
    success_message = checkout_page.get_success_message()

    assert success_message == "Thank you for your order!"