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

def get_details_of_garden(dom):
    try:
        garden=dom.xpath("listing-features__description listing-features__description--garden")[0]
        print(garden)

    except Exception as e:
        garden="Details of garden is not available"
        print(garden)


get_details_of_garden(dom)

