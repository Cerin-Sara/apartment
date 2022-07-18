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

for i in range (1,23):
    page_url=base_url + str(i)
    pages_url.append(page_url)

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

def get_title(list_url):
    listing_response=requests.get(list_url, headers=header)
    soup = BeautifulSoup(listing_response.text,'lxml')
    dom = et.HTML(str(soup))
    try:
        title=dom.xpath("//h1[@class='listing-detail-summary__title']/text()")
        title_split=title.split(":")
        title=title_split[1]
        print(title[0])

    except Exception as e:
        title = "Title is not available"

for i in listing_url:
    listing_response=requests.get(page_url, headers=header)
    soup = BeautifulSoup(listing_response.text,'lxml')
    dom = et.HTML(str(soup))
    get_title(i)

