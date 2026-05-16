import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.driver_factory import DriverFactory


@pytest.fixture
def driver():
    driver = DriverFactory().get_driver()
    yield driver
    driver.quit()


def test_add_product_to_cart(driver):

    # Login
    login_page = LoginPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    # Products Page
    products_page = ProductsPage(driver)

    products_page.add_backpack_to_cart()

    # Validate cart count
    assert products_page.get_cart_count() == "1"

    # Open cart
    products_page.open_cart()

    # Cart Page
    cart_page = CartPage(driver)

    # Validate product name
    assert cart_page.get_product_name() == "Sauce Labs Backpack"