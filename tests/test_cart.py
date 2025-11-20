import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def test_add_to_cart_flow(browser, base_url, wait):
    browser.get(base_url)
    try:
        add_links = wait.until(EC.presence_of_all_elements_located((By.LINK_TEXT, "Add to Cart")))
        add_links[0].click()
    except TimeoutException:
        browser.save_screenshot("add_to_cart_flow_timeout.png")
        raise

    browser.get(f"{base_url}/cart")
    cart_items = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "li")))
    assert len(cart_items) > 0


def test_add_multiple_items(browser, base_url, wait):
    browser.get(base_url)
    try:
        for _ in range(3):
            add_links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-test='add-to-cart']")))
            add_links[0].click()
            time.sleep(0.5)
    except TimeoutException:
        browser.save_screenshot("add_multiple_items_timeout.png")
        raise

    browser.get(f"{base_url}/cart")
    cart_items = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "li")))
    assert len(cart_items) >= 3