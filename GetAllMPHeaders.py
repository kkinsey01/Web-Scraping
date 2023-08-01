import mechanicalsoup
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://en.wikipedia.org/wiki/Main_Page"
browser = mechanicalsoup.Browser()
html = browser.get(url)
soup = html.soup

h2_elements = soup.find_all("h2", class_="mp-h2")
for head in h2_elements:
    span = head.find_all("span", class_="mw-headline")
    for text in span:
        print(text.string)