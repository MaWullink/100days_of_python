from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

sleep(2)

# Choose Language
driver.find_element(By.ID, "langSelect-EN").click()

sleep(2)

# Accept Cookies
driver.find_element(By.CLASS_NAME, "cc_btn_accept_all").click()

big_cookie = driver.find_element(By.ID, "bigCookie")
cookies = driver.find_element(By.ID, "cookies")

while True:
    big_cookie.click()

    cookie_count = int(cookies.text.split()[0].replace(",", ""))

    unlocked_products = driver.find_elements(
        By.CSS_SELECTOR,
        ".product.unlocked"
    )

    if unlocked_products:
        most_expensive_product = unlocked_products[-1]

        price = int(
            most_expensive_product.find_element(By.CLASS_NAME, "price")
            .text
            .replace(",", "")
        )

        if cookie_count >= price:
            most_expensive_product.click()










