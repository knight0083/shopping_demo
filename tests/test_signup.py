import time
import uuid
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_signup_success(browser, base_url, wait):
    username = f"user_{uuid.uuid4().hex[:6]}"
    password = "securePass123"

    browser.get(f"{base_url}/signup")
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
    browser.find_element(By.NAME, "password").send_keys(password)
    browser.find_element(By.XPATH, "//button[text()='Signup']").click()
    time.sleep(1)

    # 회원가입 성공 시 URL이 signup이 아니어야 함
    assert "signup" not in browser.current_url.lower()


def test_signup_then_login(browser, base_url, wait):
    username = f"user_{uuid.uuid4().hex[:6]}"
    password = "securePass123"

    # 회원가입
    browser.get(f"{base_url}/signup")
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
    browser.find_element(By.NAME, "password").send_keys(password)
    browser.find_element(By.XPATH, "//button[text()='Signup']").click()
    time.sleep(1)

    # 로그인
    browser.get(f"{base_url}/login")
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
    browser.find_element(By.NAME, "password").send_keys(password)
    browser.find_element(By.XPATH, "//button[text()='Login']").click()

    welcome_text = wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Welcome')]"))).text
    assert f"Welcome, {username}!" in welcome_text