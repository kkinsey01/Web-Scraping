import mechanicalsoup
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Python"
base_url = "https://en.wikipedia.org"
browser = mechanicalsoup.Browser()
page = browser.get(url)
soup = page.soup

divparent = soup.find("div", id="bodyContent")      # Finds div on given wiki page that contains the content
links = divparent.find_all("a")     # Finds all the links
for link in links:
    link_url = base_url + link["href"]      # Get each link, base URL + current link's href
    print(link_url)     # Print the current link