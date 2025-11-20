from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):
    PAY_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def open_checkout(self):
        return self.open("/checkout")

    def pay_now(self):
        self.click(self.PAY_BUTTON)