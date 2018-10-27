import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from collections import OrderedDict
import json
import codecs

def crawler(keyword):

    searchresult = list()

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 OPR/56.0.3051.43'}

    res=requests.get("https://www.bing.com/search?q="+keyword,headers=headers)


    parser = BeautifulSoup(res.text,"html.parser")

    # print(res.text)
        
    titlegroup = parser.findAll('li',attrs={'class','b_algo'})
    print("bing: "+str(len(titlegroup)))

    for t in titlegroup:

        eachresult = OrderedDict()

        eachresult["title"] = t.find('h2').text
        eachresult["href"] = t.find('h2').find('a')['href']
        eachresult["brief"] = t.find('div',attrs={'class','b_caption'}).text

        searchresult.append(eachresult)

        # print(eachresult["title"])
        # print(eachresult["href"])
        # print(eachresult["brief"])
        # print("\n","-----------------------------------\n")
   
    return searchresult



if __name__ == '__main__':
    crawler("賴清德")
