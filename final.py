from ast import Try
from bs4 import BeautifulSoup
import requests
from csv import writer
import time
import random
from lxml import etree as et

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36"}
base_url= "https://www.pararius.com/apartments/amsterdam/page-"
pages_url=[]
listing_url=[]

for i in range (1,23): #generate all the pages url
    page_url=base_url + str(i)
    pages_url.append(page_url) #append the page url to the list

def get_listing_url(page_url):
    response = requests.get(page_url, headers=header)
    soup = BeautifulSoup(response.text,'lxml')
    dom = et.HTML(str(soup))
    page_link_list=dom.xpath('//a[@class="listing-search-item__link listing-search-item__link--title"]/@href')
    for page_link in page_link_list:
        listing_url.append("https://www.pararius.com"+page_link)
    #print(listing_url)

for i in pages_url: 
    get_listing_url(i)
    time.sleep(random.randint(1,3))

def get_title(dom):    #get the title of the listing
    try:                #try to get the title
        title=dom.xpath("//h1[@class='listing-detail-summary__title']/text()")  #get the title using xpath
        title_each=title[0]
        print(title_each[10:-13]) #slicing to get only the title of the apartment

    except Exception as e: #if the title is not found, print the error message
        title = "Title is not available"

for list_url in listing_url: #get the each link from the listing_url
    listing_response=requests.get(list_url, headers=header)
    listing_soup = BeautifulSoup(listing_response.text,'lxml')
    listing_dom = et.HTML(str(listing_soup))
    get_title(listing_dom)  #calling the get_title() to execute the scraping of title