import requests
from dotenv import load_dotenv
import os

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = os.getenv("API_KEY")
NEWS_API_KEY = os.getenv("GET_NEWS_API_KEY")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Get stock data from tesla, from yesterday and the day before
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY
}

res = requests.get(STOCK_ENDPOINT, params=params)
data = res.json()
print(data)
daily_data = data["Time Series (Daily)"]
dates = list(daily_data.keys())

yesterday_close = float(daily_data[dates[0]]["4. close"])
day_before_close = float(daily_data[dates[1]]["4. close"])

percentage_difference = abs((yesterday_close - day_before_close) / day_before_close * 100)


# If the difference is bigger than 5 percent get news articles
if percentage_difference >= 5:

    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    res = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = res.json()

    # Get first 3 articles
    articles = news_data["articles"][:3]

    # Create list with headlines and descriptions
    news_list = [
        {
            "headline": article["title"],
            "description": article["description"]
        }
        for article in articles
    ]

    # Print every article in the console
    for article in news_list:
        if yesterday_close > day_before_close:
            emoji = "🔺"
        else:
            emoji = "🔻"

        print(
            f"{STOCK_NAME}: {emoji}{round(percentage_difference)}%\n"
            f"Headline: {article['headline']}\n"
            f"Brief: {article['description']}\n"
        )

else:
    print(f"No big movement in {STOCK_NAME}. Difference was {round(percentage_difference, 2)}%")