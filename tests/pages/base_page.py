from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.wait = WebDriverWait(browser, 10)

    def open(self, path=""):
        self.browser.get(f"{self.base_url}{path}")
        return self

    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()
        return el

    def type(self, locator, text):
        el = self.wait.until(EC.presence_of_element_located(locator))
        el.clear()
        el.send_keys(text)
        return el

    def text_present(self, text):
        return text in self.browser.page_source

    def get_elements(self, locator):
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.browser.find_elements(*locator)