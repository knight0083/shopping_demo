import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_login_success(browser, base_url, wait):
    browser.get(f"{base_url}/login")
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("test_user")
    browser.find_element(By.NAME, "password").send_keys("1234")
    browser.find_element(By.XPATH, "//button[text()='Login']").click()

    # 로그인 성공 후 index 페이지에서 사용자 이름 표시 확인
    welcome_text = wait.until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Welcome')]"))
    ).text
    assert "Welcome, test_user!" in welcome_text


def test_login_fail(browser, base_url, wait):
    browser.get(f"{base_url}/login")
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("wrong_user")
    browser.find_element(By.NAME, "password").send_keys("wrong_pass")
    browser.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(1)

    # 실패 시 여전히 login 페이지에 머무름
    assert browser.current_url == f"{base_url}/login"