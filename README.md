# Web-Scraping

Hello, this is my collection of Python scripts to web scrape different websites and data. 
All the scripts are well commented and the url in listed in each script.

I learned how to webscrape from this article https://realpython.com/python-web-scraping-practical-introduction/ and two of these programs are from the article. RealTimeWebScraping and SubmitFormCheck are both from this article. 

For a quick run down of each file:

AmazonScrape.py; This program looks at a product given a linkon Amazon's website (in this case, a Nvidia graphics card). Then, will extract the product's title, rating, price, and grabs the prices of the items that Amazon lists as similiar to the item you are viewing. 

GetAllLinks.py; This program will find all the links for "Python" search on the wiki. It will print the entire link, so each anchor tags href and the base url for wiki

GetAllMPHeaders.py; This program will look at the Wiki's main page and extract then print all the headers on the page

RealTimeWebScraping.py; This program reloads a dice roll simulator every 10 seconds for 4 times (just to keep it simple). After each page refresh, will print the random dice roll that the page shows. 

SubmitFormCheck.py; This program is given a webpage, and a correct username and password. It will then take the data and insert it into the form and submit the form. 
