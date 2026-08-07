import os
import requests

from bs4 import BeautifulSoup
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
load_dotenv()

# ---------------------Scrape Data -----------------------------
zillow_url = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(url=zillow_url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
photo_cards_data = [
    {
        "address": card.select_one("address").get_text(strip=True),
        "link": card.select_one("a")["href"],
        "price": card.select_one(".PropertyCardWrapper__StyledPriceLine").get_text(strip=True),
    }
    for card in soup.select(".StyledPropertyCardDataWrapper")
]

print(photo_cards_data)

# -------------------Put data in google forms---------------------------
FORM_LINK = os.environ["FORM_LINK"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

for card in photo_cards_data:
    driver.get(FORM_LINK)

    sleep(2)

    inputs = driver.find_elements(
        By.CSS_SELECTOR,
        "input[jsname='YPqjbf']"
    )

    inputs[0].send_keys(card["address"])
    inputs[1].send_keys(card["price"])
    inputs[2].send_keys(card["link"])

    send_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(text(),'Verzenden')]/ancestor::div[@role='button']")
        )
    )
    send_btn.click()

    sleep(2)
