import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.upload_speed = 0
        self.download_speed = 0
        self.wait = WebDriverWait(self.driver, 120)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    '[aria-label="start speed test - connection type multi"]'
                )
            )
        )

        button.click()

        speeds = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "h3.font-mono.text-5xl")
            )
        )

        self.download_speed = speeds[0].text
        self.upload_speed = speeds[1].text

    def tweet_at_provider(self):
        pass

    def close_browser(self):
        self.driver.quit()
