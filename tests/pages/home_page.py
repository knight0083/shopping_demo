from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    PRODUCTS = (By.CSS_SELECTOR, "ul li")
    VIEW_CART = (By.LINK_TEXT, "View Cart")

    def open_home(self):
        return self.open("/")

    def list_products(self):
        return self.get_elements(self.PRODUCTS)

    def go_to_cart(self):
        self.click(self.VIEW_CART)