import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from collections import OrderedDict
import json
import codecs

def crawler(keyword):
    
    searchresult = list()

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 OPR/56.0.3051.43'}

    res=requests.get("https://www.google.com/search?q="+keyword,headers=headers)

    parser = BeautifulSoup(res.text,"html.parser")

    # print(res.text)
        
    titlegroup = parser.findAll('div',attrs={'class','rc'})

    print(len(titlegroup))

    for t in titlegroup:

        eachresult = OrderedDict()

        eachresult["title"] = t.find('div',attrs={'class','r'}).find('h3',attrs={'class','LC20lb'}).text
        eachresult["href"] = t.find('div',attrs={'class','r'}).find('a')['href']
        eachresult["brief"] = t.find('div',attrs={'class','s'}).text

        searchresult.append(eachresult)

        # print(eachresult["title"])
        # print(eachresult["href"])
        # print(eachresult["brief"])
        # print("\n","-----------------------------------\n")
   
    return searchresult



if __name__ == '__main__':
    crawler("台南市長")
