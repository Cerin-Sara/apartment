from ast import Try
from bs4 import BeautifulSoup
import requests
from csv import writer
import time
import random
from lxml import etree as et

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36"} #adding user agents to avoid detection
base_url= "https://www.pararius.com/apartments/amsterdam/page-" #base url for the pages
pages_url=[]    #list to store the url of every page
listing_url=[]  #list to store the url of every apartments

for i in range (1,23): #generate all the pages url
    page_url=base_url + str(i)
    pages_url.append(page_url) #append the page url to the list

def get_listing_url(page_url):  #get the url of the listing
    response = requests.get(page_url, headers=header)
    soup = BeautifulSoup(response.text,'lxml')
    dom = et.HTML(str(soup))
    page_link_list=dom.xpath('//a[@class="listing-search-item__link listing-search-item__link--title"]/@href')
    for page_link in page_link_list:
        listing_url.append("https://www.pararius.com"+page_link)
    #print(listing_url)

for apge_url in pages_url:     #for each page url, get the listing url
    get_listing_url(page_url)
    time.sleep(random.randint(1,3))

def get_title(dom):    #get the title of the listing
    try:                #try to get the title
        title=dom.xpath("//h1[@class='listing-detail-summary__title']/text()")  #get the title using xpath
        title_each=title[0]
        print(title_each[10:-13]) #slicing to get only the title of the apartment

    except Exception as e: #if the title is not found, print the error message
        title = "Title is not available"

def get_location(dom):  #get the location of the listing
    try:            #try to get the location
        location= dom.xpath("//div[@class='listing-detail-summary__location']/text()")
        print(location[0])  #print the location
    except Exception as e:      #if the location is not found, print the error message
        location = "Location is not available"

def get_price(dom):         #get the price of the listing
    try:                    #try to get the price
        price=dom.xpath("//div[@class='listing-detail-summary__price']/text()")
        price =price[0].replace('€', '').replace(',', '').replace('\n', '').strip() #remove the €, comma and new line, retrieving the value
        print(price)    #printing both the strings
        
    except Exception as e:          #if the price is not found, print the error message
        price = "Price is not available"

for list_url in listing_url: #get the each link from the listing_url
    listing_response=requests.get(list_url, headers=header)
    listing_soup = BeautifulSoup(listing_response.text,'lxml')
    listing_dom = et.HTML(str(listing_soup))
    get_title(listing_dom)  #calling the get_title() to execute the scraping of title
    get_location(listing_dom)   #calling the get_location() to execute the scraping of location
    get_price(listing_dom)   #calling the get_price() to execute the scraping of price