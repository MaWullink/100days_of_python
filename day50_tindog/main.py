import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

# Setup Chrome profile
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://app.100daysofpython.dev/services/tindog/u/bAPBj5-FxBPaBsoo4s2j4zbuwAsnknZJ"
)

wait = WebDriverWait(driver, 10)

# Like profiles
while True:
    like_button = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-like"))
    )



