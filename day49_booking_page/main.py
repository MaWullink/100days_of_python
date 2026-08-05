import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# ----------------  Step 1 - Setup, Chrome Profile and Basic Navigation ----------------

USER_NAME = "Malene"
USER_EMAIL = "mw@test.com"
USER_PASSWORD = "testing"

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://appbrewery.github.io/gym/")


# ----------------  Step 2 - Automated Login ----------------

wait = WebDriverWait(driver, 10)

login_btn = wait.until(
    EC.element_to_be_clickable((By.ID, "login-button"))
)
login_btn.click()


email_input = wait.until(
    EC.presence_of_element_located((By.ID, "email-input"))
)
email_input.send_keys(USER_EMAIL)


password_input = wait.until(
    EC.presence_of_element_located((By.ID, "password-input"))
)
password_input.send_keys(USER_PASSWORD)


submit_btn = wait.until(
    EC.element_to_be_clickable((By.ID, "submit-button"))
)
submit_btn.click()


# Wait until schedule loads
wait.until(
    EC.presence_of_element_located((By.ID, "schedule-page"))
)


# ----------------  Step 3 - Choose and Book Class ----------------

print("Welcome to the booking page 🤗")

day = input("Which day do you want to book your workout? ")
class_type = input("Which class do you want to take? (Yoga/Spin/HIIT) ")
time = input("Which time? (HH:MM) ")


# Convert input to website format
day = day.lower()[:3]          # Tuesday -> tue
class_type = class_type.lower()
format_time = time.replace(":", "")  # 18:00 -> 1800


try:
    class_card = wait.until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                f"[id^='day-group-{day}'] [data-class-type='{class_type}'][id$='{format_time}']"
            )
        )
    )

    class_button = class_card.find_element(By.TAG_NAME, "button")


    if class_button.text == "Booked":
        print("✓ You already booked this class 🤗")


    elif class_button.text == "Waitlisted":
        print("✓ You are already on the waitlist 🤗")


    elif class_button.text == "Join Waitlist":
        class_button.click()
        print(f"✓ Joined waitlist for {class_type.title()} on {day.title()} at {time}")


    else:
        class_button.click()
        print(f"✓ Booked {class_type.title()} on {day.title()} at {time}")


except TimeoutException:
    print("❌ Could not find this class")