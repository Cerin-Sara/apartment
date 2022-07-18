from ast import Try
from bs4 import BeautifulSoup
import requests
from lxml import etree as et

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36"}
page_url="https://www.pararius.com/apartment-for-rent/amsterdam/1b402016/eerste-boerhaavestraat"

listing_response=requests.get(page_url, headers=header)
soup = BeautifulSoup(listing_response.text,'lxml')
dom = et.HTML(str(soup))

#****************OFFERED SINCE****************

def get_no_floors(dom):
    try:
        no_floors=dom.xpath("//dd[@class='listing-features__description listing-features__description--number_of_floors']/span/text()")[0]
        print(no_floors)

    except Exception as e:
        no_floors="Number of floors is not available"
        print(no_floors)


get_no_floors(dom)

