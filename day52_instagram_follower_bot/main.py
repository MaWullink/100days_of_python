import os

from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

load_dotenv()

TARGET_ACCOUNT = "rordongamsay"
USERNAME = os.environ["USERNAME_INSTA"]
PASSWORD = os.environ["PASSWORD_INSTA"]
BASE_URL = "https://app.100daysofpython.dev/services/share-a-naan"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)

    def login(self):
        self.driver.get(BASE_URL)

        username = self.wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username.send_keys(USERNAME)

        password = self.wait.until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password.send_keys(PASSWORD)

        login_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".naan-welcome-submit"))
        )
        login_btn.click()

        try:
            dismiss_btn = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".naan-popup-dismiss"))
            )
            dismiss_btn.click()
        except TimeoutException:
            pass

        try:
            notification_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))
            )
            notification_btn.click()
        except TimeoutException:
            pass

    def find_followers(self):
        search_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-naan-search-toggle]"))
        )
        search_btn.click()

        search_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".naan-search-input"))
        )
        search_input.send_keys(TARGET_ACCOUNT)
        sleep(2)
        search_input.send_keys(Keys.ENTER)

        followers_link = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".naan-followers-link"))
        )
        followers_link.click()

    def follow(self):
        all_buttons = self.driver.find_elements(
            By.CSS_SELECTOR,
            ".followers-scroll button:not(.is-following)"
        )

        for button in all_buttons:
            button.click()
            sleep(1)

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
