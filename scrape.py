import time
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
from contextlib import suppress


# Initialize browser
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

urlList = []

# Initialize browser
browser = init_browser()

# Visit Costa Rica surf site
url = "'https://www.billboard.com/archive/charts/{0}/hot-100".format(year)
browser.visit(url)

# Scrape page into soup
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

# selenium

#for i in td, tr, href, select that link then scrape that page and put name and artist into the list and then go back and do it again f
#again for each issue of the year. then move to the next page and do it again. then we'll use the db to input info in the search function for bpm key length genre

# Find today's surf conditions

table = soup.find('table', class_ = 'archive-table')
url = table.find_all('a', href = True)         #, class_ = 'sl-spot-list__ref'
for i in url:
    urlList.append(i.text)

print('dopeshit')
print(name)

# for i in spot_list:
#     location.append(i.find("h3", class_ = "sl-spot-details__name").text)
#     surf_height.append(i.find("span", class_="quiver-surf-height").text)
#     link.append(i.find("a", class_ = "sl-cam-list-link").get('href'))
# print('fuckthisshit')
#
# temp_list = []
# link_url = 'https://www.surfline.com'
# for i in link:
#     browser.visit(link_url + i)
#     html = browser.html
#     soup = BeautifulSoup(html, 'html.parser')
#     temp_list.append(soup.find("div", class_="sl-wetsuit-recommender__weather").text)
#     print('link_url + i')

# water_temp = []
# air_temp = []
# for i in temp_list:
#     water_temp.append(i[:-5])
#     air_temp.append(i[-5:])
#
# water_temp = temp[:-5]
# air_temp = temp[-5:]
# print(water_temp)
# print(air_temp)

# full_url=[]
# for i in link:
#     full_url.append(link_url + i)
# print('osfds')

# listlesssss = []
# j = 0
# while j < 54:
#     fivesurf = {
#         "Title": title[j],
#             "Artist": artist[j],
#             'Key': key[j],
#             #'BPM': bpm[j],
#             #'Genre': genre[j]
#             #'Length' length(j)    just artist and key for now from the billboard website
#             }
#             listlesssss.append(fivesurf)
# j += 1
#     print(j)

# Module used to connect Python with MongoDb
import pymongo

# The default port used by MongoDB is 27017
# https://docs.mongodb.com/manual/reference/default-mongodb-port/
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define the 'classDB' database in Mongo
db = client.billboard


# Insert a document into the 'students' collection

# for i in listlesssss:
#
# db.(year).(issueDate).(position).insert_one(i)   (this is for all the shit in i)
#
# db.surf_summary.insert_one(i)
