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
        title=title[0]
        title=title[10:-13]
        print(title, "title") #slicing to get only the title of the apartment

    except Exception as e: #if the title is not found, print the error message
        title = "Title is not available"
        print(title)

def get_location(dom):  #get the location of the listing
    try:            #try to get the location
        location= dom.xpath("//div[@class='listing-detail-summary__location']/text()")
        location=location[0]
        print(location, "location")  #print the location
    except Exception as e:      #if the location is not found, print the error message
        location = "Location is not available"
        print(location)

def get_price(dom):         #get the price of the listing
    try:                    #try to get the price
        price=dom.xpath("//div[@class='listing-detail-summary__price']/text()")
        price =price[0].replace('€', '').replace(',', '').replace('\n', '').strip() #remove the €, comma and new line, retrieving the value
        print(price,'price')    #printing both the strings
        
    except Exception as e:          #if the price is not found, print the error message
        price = "Price is not available"
        print(price)

def get_area(dom):         #get the area of the listing
    try:                    #try to get the area
        area=dom.xpath("//li[@class='illustrated-features__item illustrated-features__item--surface-area']/text()")
        area=area[0].replace("m²","").replace(" ","")   #remove the m² and space, retrieving the value
        print(area,'area')

    except Exception as e:      #if the area is not found, print the error message
        area="Area is not available"
        print(area)

def get_rooms(dom):
    try:
        rooms=dom.xpath("//li[@class='illustrated-features__item illustrated-features__item--number-of-rooms']/text()")
        rooms=rooms[0].split(" ")[0]
        print(rooms,'rooms')
    except Exception as e:
        rooms="Rooms is not available"
        print(rooms)

def get_interior(dom):              #get the interior status of the listing
    try:
        interior = dom.xpath("//li[@class='illustrated-features__item illustrated-features__item--interior']/text()")
        interior = interior[0]
        print(interior,'interior')
    except  Exception as e:
        interior= "Interior is not available" #if the interior is not found, print the error message
        print(interior)


def get_description(dom):           #get the description of the listing
    try:
        description = dom.xpath("//div[@class='listing-detail-description__additional listing-detail-description__additional--collapsed']/p/text()")
        description = description[0]
        print(description,'description')
    except Exception as e:              #if the description is not found, print the error message
        description= "Description is not available"
        print(description)

def offered_since(dom):         #get the date since the listing was added
    try:
        offer_since=dom.xpath("//dd[@class='listing-features__description listing-features__description--offered_since']/span/text()")
        offer_since=offer_since[0]
        print(offer_since,'offer_since')
    except Exception as e:          #if the date is not found, print the error message
        order_since= "Order since is not available"
        print(order_since)

def get_availability(dom):          #get the availability of the listing
    try:
        available_from=dom.xpath("//dd[@class='listing-features__description listing-features__description--acceptance']/span/text()")
        available_from=available_from[0].split(" ")[1]      
        print(available_from,'available_from')

    except Exception as e:              #if the availability is not found, print the error message
        print("Not available to book")

def get_specification(dom):          #get the specification of the listing
    try:                                #try to get the specification
        specifics = dom.xpath("//dd[@class='listing-features__description listing-features__description--specifics']/span/text()")
        specifics = specifics[0]
        print(specifics,'specifics')

    except Exception as e:              #if the specification is not found, print the error message
        specifics="Specifics are not available"
        print(specifics)


def get_upkeep_status(dom):             #get the upkeeping status of the listing
    try:                                #try to get the upkeeping status
        upkeep=dom.xpath("//dd[@class='listing-features__description listing-features__description--upkeep']/span/text()")
        upkeep=upkeep[0]
        print(upkeep,'upkeep')

    except Exception as e:              #if the upkeeping status is not found, print the error message
        upkeep = "Upkeep is not available"
        print(upkeep)

for list_url in listing_url: #get the each link from the listing_url
    listing_response=requests.get(list_url, headers=header)
    listing_soup = BeautifulSoup(listing_response.text,'lxml')
    listing_dom = et.HTML(str(listing_soup))
    get_title(listing_dom)  #calling the get_title() to execute the scraping of title
    get_location(listing_dom)   #calling the get_location() to execute the scraping of location
    get_price(listing_dom)   #calling the get_price() to execute the scraping of price
    get_area(listing_dom)   #calling the get_area() to execute the scraping of area
    get_rooms(listing_dom)   #calling the get_rooms() to execute the scraping of rooms
    get_interior(listing_dom)   #calling the get_interior() to execute the scraping of interior
    get_description(listing_dom)   #calling the get_description() to execute the scraping of description
    offered_since(listing_dom)   #calling the ordered_since() to execute the scraping of order_since
    get_availability(listing_dom)   #calling the get_availability() to execute the scraping of availability
    get_specification(listing_dom)   #calling the get_specification() to execute the scraping of specification
    get_upkeep_status(listing_dom)   #calling the get_upkeep_status() to execute the scraping of upkeeping status