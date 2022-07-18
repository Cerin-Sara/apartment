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

def get_location_type(dom):
    try:
        location_type=dom.xpath("//dd[@class='listing-features__description listing-features__description--situations']/span/text()")[0]
        print(location_type)

    except Exception as e:
        location_type="Location type is not available"
        print(location_type)


get_location_type(dom)

