from ast import Try
from bs4 import BeautifulSoup
import requests
from lxml import etree as et


header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36"}
page_url="https://www.pararius.com/apartment-for-rent/amsterdam/1b402016/eerste-boerhaavestraat"


listing_response=requests.get(page_url, headers=header)
soup = BeautifulSoup(listing_response.text,'lxml')
dom = et.HTML(str(soup))

def get_area():
    try:
        area=dom.xpath("//li[@class='illustrated-features__item illustrated-features__item--surface-area']/text()")
        area=area[0].replace("m²","").replace(" ","")
        print(area)

    except Exception as e:
        area="Area is not available"