import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.nl/-/en/Misilmp-Telescope-Including-Refractor-Beginners/dp/B0CT8WDJWZ/?_encoding=UTF8&pd_rd_w=9KIAt&content-id=amzn1.sym.891c33ba-9d81-462d-97fa-04938c1990db&pf_rd_p=891c33ba-9d81-462d-97fa-04938c1990db&pf_rd_r=42GDH5J1XNFY7J02QCE4&pd_rd_wg=Hxhjx&pd_rd_r=d0f7b84b-1aae-489a-9f08-ae3bfdca7642&ref_=pd_hp_d_r_atf_dealz_wd_sv&th=1"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/138.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

BUY_PRICE = 60

response = requests.get(URL, headers=HEADERS)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

price = soup.select_one(".a-offscreen").get_text()
price_as_float = float(price.split("€")[1])

title = soup.select_one("#productTitle").get_text().strip()
short_title = " ".join(title.split()[:4])


if price_as_float < BUY_PRICE:
    message = f"{short_title} is on sale for {price}!"
    print(message)
else:
    print(f"{short_title} is still too expensive. Current price: {price}")


