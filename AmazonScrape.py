import requests
from bs4 import BeautifulSoup

base_url = "https://www.amazon.com"
url = "https://www.amazon.com/ZOTAC-GeForce-Graphics-IceStorm-ZT-A30600H-10M/dp/B08W8DGK3X/ref=psdc_284822_t1_B0971BG25M"

HEADERS = {
    "User-Agent": ("Mozilla/5.0 (X11; Linux x86_64)"
                   "AppleWebKit/537.36 (KHTML, like Gecko)"
                   "Chrome/44.0.2403.157 Safari/537.36"),
    "Accept-Language": "en-US, en;q=0.5"
}

html = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(html.text, features="lxml")
title = soup.find("span", {"id":"productTitle"}).text.strip()       # Find title of given product
print(title)

price = soup.find("span", {"class":"a-offscreen"}).text.strip()     # Find price that is on the right side of the screen for product
print(price)

rating = soup.find("span", {"class": "a-icon-alt"}).text.strip()    # Find overall rating
print(rating)

price_row = soup.find("tr", {"id": "comparison_price_row"})     # Find div containing table of similiar items and their prices

for i in range(4):
    selector = (f"td:nth-child({i}) > span:first-child > span:first-child")
    selected_price = price_row.select(f"td:nth-child({i}) > span:first-child > span:first-child")       # Find price of column item
    if selected_price:
        print(selected_price)

prices = [a.text.strip() for a in price_row.select("td > span:first-child > span:first-child")]     # For testing purposes, prints array of prices from table 
print(prices)
