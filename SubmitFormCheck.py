import mechanicalsoup

browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
page = browser.get(url)
page_html = page.soup

form = page_html.form
form.select("input")[0]["value"] = "zeus"       # Username
form.select("input")[0]["value"] = "ThunderDude"        # Password

profiles_page = browser.submit(form, page.url)      # Submits the form on webpage with given values
title = profiles_page.soup.select("title")
print(title)

print(title[0].text)