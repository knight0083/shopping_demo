from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    ITEMS = (By.CSS_SELECTOR, "ul li")
    CHECKOUT = (By.LINK_TEXT, "Checkout")

    def open_cart(self):
        return self.open("/cart")

    def items(self):
        return self.get_elements(self.ITEMS)

    def go_to_checkout(self):
        self.click(self.CHECKOUT)