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
# available_from=dom.xpath("//dd[@class='listing-features__description listing-features__description--acceptance']/span/text()")[0].split(" ")[1]      
# print(available_from)

# def get_contact_details(dom):
#     try:
#         contact_details=dom.xpath("//a[@class='agent-summary__agent-contact-request']/@href")[0]
#         contact_details="https://www.pararius.com"+contact_details
#         print(contact_details)


#     except Exception as e:
#         contact_details="Details of contact is not available"
#         print(contact_details)


# get_contact_details(dom)



volume= dom.xpath("//dd[@class='listing-features__description listing-features__description--volume']/span/text()")[0].split(" ")[0]
print(volume)
