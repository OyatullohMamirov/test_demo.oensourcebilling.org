from selenium.webdriver.common.by import By
import time
from config import driver, wait, ec

url = 'https://demo.opensourcebilling.org/en/users/sign_in'
driver.get(url)

username_enter = 'demo@opensourcebilling.org'
password_enter = 'password'

try:
    username = driver.find_element(By.ID, value="email")
    username.clear()
    username.send_keys(username_enter)
    print("✓ Username entered successfully")
    password = driver.find_element(By.ID, value="password")
    if not password:
        password = driver.find_element(By.NAME, value="user[password]")
    password.clear()
    password.send_keys(password_enter)
    print("✓ Password entered successfully")

    submit = driver.find_element(By.ID, value="user_login_btn")
    submit.click()
    print(" Login button clicked")
    expected_dashboard_url = "https://demo.opensourcebilling.org/en/dashboard"
    wait.until(ec.url_to_be(expected_dashboard_url))
    current_url = driver.current_url
    if current_url == expected_dashboard_url:
        print("\n LOGIN SUCCESSFUL: URL redirected to dashboard")
        print(f"Current URL: {current_url}")

        try:
            dashboard_element = wait.until(
                ec.presence_of_element_located((By.CSS_SELECTOR, ".container-fluid, .main")))
            print("Dashboard element found: " + dashboard_element.text)
        except:
            print("Dashboard element not found, but URL indicates successful login")
    else:
        print("\n LOGIN FAILED: URL did not redirect to dashboard")
        print(f"Current URL: {current_url}")

        try:
            error_message = driver.find_element(By.CSS_SELECTOR, ".alert, .error-message")
            print("Error message displayed: " + error_message.text)
        except:
            print("No specific error message found")

except Exception as e:
    print(f"\nAn error occurred during the login process: {str(e)}")

screenshot_path = "login_result.png"
driver.save_screenshot(screenshot_path)
print(f"\nScreenshot saved to {screenshot_path}")
time.sleep(5)