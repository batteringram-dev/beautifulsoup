'''

This is a simple web scraping project where we scrape the details of certain houses
located in Amsterdam. The details are on the website - Pararius 

Scraping is done using the library - BeautifulSoup and then the data is loaded 
into a csv ( Comma Seperated Values ) file.

'''

# importing libraries
import requests
from bs4 import BeautifulSoup
from csv import writer

# creating a connection to the website
url = "https://www.pararius.com/apartments/amsterdam?ac=1"
con = requests.get(url)
print("Response: ", con) # if response - 200, then the connection is successful

# bs4 context
soup = BeautifulSoup(con.content, "html.parser")
lists = soup.find_all("section", class_="listing-search-item")

# iteration and writing the data to a csv file
with open('housingdetails.csv', 'w', encoding = 'utf8', newline = '') as f:
    thewriter = writer(f)
    header = ['Title', 'Location', 'Price']
    thewriter.writerow(header)
    
    '''iterating through every details in the page'''
    for list in lists:
        title = list.find('a', class_="listing-search-item__link--title").text.replace('\n', '')
        location = list.find('div', class_="listing-search-item__sub-title").text.replace('\n', '')
        price = list.find('div', class_="listing-search-item__price").text.replace('\n', '')

        info = [title, location, price]
        thewriter.writerow(info)