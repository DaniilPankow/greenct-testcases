import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.greencity.cx.ua/#/greenCity"


class TestSignUp(unittest.TestCase):

    def setUp(self):
        """Preconditions: запуск браузера"""
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        """Закриття браузера"""
        self.driver.quit()

    def test_user_can_sign_up(self):
        """Тест: успішна реєстрація користувача"""

        driver = self.driver
        wait = self.wait

        # Генерація унікального email
        email = f"test{int(time.time())}@gmail.com"

        # 1. Натиснути "Sign up"
        sign_up_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Sign up']"))
        )
        sign_up_button.click()

        # 2. Ввести email
        email_input = wait.until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email_input.send_keys(email)

        # 3. Ввести login
        login_input = driver.find_element(By.ID, "firstName")
        login_input.send_keys("testuser123")

        # 4. Ввести пароль
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("Password123!")

        # 5. Підтвердити пароль
        repeat_password_input = driver.find_element(By.ID, "confirmPassword")
        repeat_password_input.send_keys("Password123!")

        # 6. Натиснути кнопку Sign up
        submit_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign up']"))
        )
        submit_button.click()

        # 7. Перевірка логіну
        success_element = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="header_user-wrp"]/li'))
        )

        self.assertTrue(success_element.is_displayed(), "Sign up failed")


if __name__ == "__main__":
    unittest.main()
