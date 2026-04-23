import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.greencity.cx.ua/#/greenCity"


class TestSignUpNegative(unittest.TestCase):

    def setUp(self):
        """Preconditions: користувач відкриває форму реєстрації"""
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
        self.wait = WebDriverWait(self.driver, 10)

        # Відкрити форму Sign up
        sign_up_button = self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "/html/body/app-root/app-main/div/app-header/header/div[2]/div/div/div/ul/li[2]/div/span"
            ))
        )
        sign_up_button.click()

    def tearDown(self):
        self.driver.quit()

    def test_password_too_short_sign_up_blocked(self):
        """Тест: неможливо зареєструватись з паролем менше 8 символів"""

        driver = self.driver
        wait = self.wait

        # 1. Email
        email_input = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="email"]'))
        )
        email_input.send_keys("test@gmail.com")

        # 2. Login
        login_input = driver.find_element(By.XPATH, '//*[@id="firstName"]')
        login_input.send_keys("testuser")

        # 3. Password (7 символів)
        password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
        password_input.send_keys("1234567")

        # 4. Repeat password
        repeat_password_input = driver.find_element(By.XPATH, '//*[@id="repeatPassword"]')
        repeat_password_input.send_keys("1234567")

        # 5. Error message
        error_message = wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                '//*[@id="mat-mdc-dialog-1"]/div/div/app-auth-modal/div/div/div[2]/div/app-sign-up/div/div[1]/form/p'
            ))
        )

        self.assertTrue(error_message.is_displayed(), "Error message not displayed")
        self.assertIn("Password", error_message.text)

        # 6. Button disabled
        sign_up_submit = driver.find_element(
            By.XPATH,
            '//*[@id="mat-mdc-dialog-1"]/div/div/app-auth-modal/div/div/div[2]/div/app-sign-up/div/div[1]/form/button'
        )

        self.assertFalse(sign_up_submit.is_enabled(), "Sign up button should be disabled")


if __name__ == "__main__":
    unittest.main()
