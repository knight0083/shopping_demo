import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_checkout_clears_cart_and_confirms_order(browser, base_url, wait):
    browser.get(base_url)
    add_links = wait.until(EC.presence_of_all_elements_located((By.LINK_TEXT, "Add to Cart")))
    add_links[0].click()
    time.sleep(1)

    browser.get(f"{base_url}/cart")
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Checkout"))).click()

    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Pay Now']"))).click()
    time.sleep(1)

    browser.get(f"{base_url}/cart")
    cart_items = browser.find_elements(By.TAG_NAME, "li")
    assert len(cart_items) == 0