from ast import Try
from bs4 import BeautifulSoup
import requests
from csv import writer
import time
import random
from lxml import etree as et


header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36"}
page_url="https://www.pararius.com/apartment-for-rent/amsterdam/1b402016/eerste-boerhaavestraat"


listing_response=requests.get(page_url, headers=header)
soup = BeautifulSoup(listing_response.text,'lxml')
dom = et.HTML(str(soup))


def get_title():
    try:
        title=dom.xpath("//h1[@class='listing-detail-summary__title']/text()")
        print(title[0])

    except Exception as e:
        title = "Title is not available"


get_title()
    





