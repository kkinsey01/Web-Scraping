import mechanicalsoup
import time
browser = mechanicalsoup.Browser()

for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]        # Find element with id #result
    result = tag.text

    print(f"The result of your dice roll is: {result}")     # Prints dice roll on current load of the webpage, gives 4 dice roll values
    if (i < 3):
        time.sleep(10)      # Get the program to refresh the page for a new dice roll every 10 seconds
