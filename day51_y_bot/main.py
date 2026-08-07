# Incomplete: Speedtest changed its website structure, making the original Selenium approach unreliable. An API would have made this much easier.
import os

from dotenv import load_dotenv

from InternetSpeedTwitterBot import InternetSpeedTwitterBot


load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 10

Y_EMAIL = os.environ["Y_EMAIL"]
Y_PASSWORD = os.environ["Y_PASSWORD"]


bot = InternetSpeedTwitterBot()

bot.get_internet_speed()
bot.tweet_at_provider()



