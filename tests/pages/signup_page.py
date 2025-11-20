from selenium.webdriver.common.by import By
from .base_page import BasePage

class SignupPage(BasePage):
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")

    def open_signup(self):
        return self.open("/signup")

    def signup(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)