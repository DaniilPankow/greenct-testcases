import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.greencity.cx.ua/#/greenCity"


class TestEcoNews(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_user_can_open_news_and_view_details(self):

        driver = self.driver
        wait = self.wait

        # 1. Eco News
        eco_news_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Eco News')]"))
        )
        eco_news_button.click()

        # 2. Список новин
        news_list = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="main-content"]//ul/li'))
        )

        self.assertTrue(len(news_list) > 0, "News list is empty")

        # 3. Перша новина
        first_news = news_list[0]
        first_news.click()

        # 4. Деталі новини
        news_content = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content"]//div[contains(@class,"news")]'))
        )

        self.assertTrue(news_content.is_displayed(), "News details not displayed")


if __name__ == "__main__":
    unittest.main()
