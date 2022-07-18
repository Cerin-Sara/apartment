from ast import Try
from bs4 import BeautifulSoup
import requests
from csv import writer
import time
import random
from lxml import etree as et

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36"}
base_url= "https://www.pararius.com/apartments/amsterdam/page-"
url=[]
i=1
while i <23:
    page_url=base_url + str(i)
    #print(page_url)
    url.append(page_url)
    
    res= requests.get(page_url, headers=header)
    soup = BeautifulSoup(res.text,'lxml')
    
    #dom = et.HTML(str(soup))
    dom = et.HTML(str(soup))
    link_to_each_house=[]
    try:
        house_url_list=dom.xpath("//h2[@class='listing-search-item__title']/a/@href")
        #house_list=soup.find_all('li',class_='search-list__item search-list__item--listing').text.strip()
        # *****************************************print("\n\n\n\n\n")
        # *****************************************print(i,"th page")
        #print(house_url_list)
        n=len(house_url_list)
        for j in range(n):
            house_url=house_url_list[j]
            #print(house_url)
            house_url="https://www.pararius.com"+house_url
            title_text=house_url.find_all('h1',class_="listing-detail-summary__title").text()
            print(title_text)
            # link_to_each_house.append(house_url) # this is for the whole list of houses
        # *****************************************print(house_url)  # this is for each house
        

            
            #house_url_list[j]=house_url
        # "https://www.pararius.com"+house_url_list[0]
        # print(link_to_each_house)
    except Exception as e:
        house_list = "houselist not available"

    i=i+1


def time_delay():
    time.sleep(random.randint(2, 5))