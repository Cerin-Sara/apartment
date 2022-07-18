from ast import Try
from bs4 import BeautifulSoup
import requests
from csv import writer
import time
import random
from lxml import etree as et
import re


header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36"}
page_url="https://www.pararius.com/apartment-for-rent/amsterdam/1b402016/eerste-boerhaavestraat"


listing_response=requests.get(page_url, headers=header)
soup = BeautifulSoup(listing_response.text,'lxml')
dom = et.HTML(str(soup))


# def get_title():
#     try:
#         title=dom.xpath("//h1[@class='listing-detail-summary__title']/text()")
#         print(title[0])

#     except Exception as e:
#         title = "Title is not available"


# get_title()
# def get_location():
#     try:
#         location= dom.xpath("//div[@class='listing-detail-summary__location']/text()")
#         print(location[0])
#     except Exception as e:
#         location = "Location is not available"

#get_location()
# def get_price():
#     try:
#         price=dom.xpath("//div[@class='listing-detail-summary__price']//text()")
#         price_each=price[0]
#         price_each=price_each.replace('\n','')
#         price_each.strip()
#         price_list=price_each.split(',')
#         price_first=price_list[0]
#         price_second=price_list[1]
#         price_first=price_first[-1]
#         price_second=price_second[:3]
#         print(price_first+price_second)
        
#         price=int(re.search(r'\d+', price_each).group())
        
        
#     except Exception as e:
#         price = "Price is not available"

# get_price()

try:
        price=dom.xpath("//div[@class='listing-detail-summary__price']/text()")
        # price_each=price[0] #get the price of the apartment
        # price_each=price_each.replace('\n','') #remove the new line character
        # price_each.strip() #removing leading and trailing characters
        # price_list=price_each.split(',') #splitting and storing in the list
        # price_first=price_list[0]   #storing the element before ','
        # price_second=price_list[1]  #storing the element after ','
        # price_first=price_first[-1] # slicing only the last character
        # price_second=price_second[:3]   #slicing the first three characters
        price =price[0].replace('€', '').replace(',', '').replace('\n', '').strip()
        print(price)    #printing both the strings
        
except Exception as e:
    price = "Price is not available"
