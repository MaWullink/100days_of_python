import smtplib
import datetime as dt
import random
import pandas as pd

MY_EMAIL = "test@gmail.com"
MY_PASSWORD = "test"

date = dt.datetime.now()
today = (date.month, date.day)

df = pd.read_csv("birthdays.csv")

birthdays_dict = {
    (data_row.month, data_row.day): data_row
    for (index, data_row) in df.iterrows()
}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as file:
        content = file.read()
        content = content.replace("[NAME]", birthday_person["name"])
        print(content)
    # with smtplib.SMTP("smtop.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    #     connection.sendmail(from_addr=MY_EMAIL, to_addrs="email2@gmail.com",
    #                         msg=f"Subject:Happy Birthday!\n\n{content}")



