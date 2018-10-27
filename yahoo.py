import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from collections import OrderedDict
import json
import codecs
import re

def crawler(keyword):

    searchresult = list()

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 OPR/56.0.3051.43'}

    res=requests.get("https://tw.search.yahoo.com/search?p="+keyword,headers=headers)
    # res = requests.get("https://tw.search.yahoo.com/search;_ylt=AwrtEFhPdNNbChAA28Nr1gt.;_ylu=X3oDMTFhdTV0M3ZoBGNvbG8DdHcxBHBvcwMxBHZ0aWQDQjU1MTlfMQRzZWMDcGFnaW5hdGlvbg--?p=鬥陣特攻&pz=14&bct=0&b=1&pz=10&bct=0&xargs=0")

    parser = BeautifulSoup(res.text,"html.parser")

    searchresultlist = parser.find('ol',class_="searchCenterMiddle").findAll('li',recursive=False)
    print("yahoo: "+str(len(searchresultlist)))

    for sr in searchresultlist:

       eachresult = OrderedDict()
        
       eachresult['title'] = sr.find('h3').text       
       # print(eachresult['title'])


       if sr.find(class_="aUrl") is None:
        eachresult['href'] = sr.find('a')['href']
        # print(eachresult['title'])
       else:
        eachresult['href'] = sr.find(class_="aUrl").text
        # print(eachresult['title'])


       if sr.find(class_='options-toggle') is not None:
        eachresult['brief'] = sr.find(class_="lh-l").text
        # print(eachresult['brief'])
       else:
        eachresult['brief'] = ""
        # print(eachresult['brief'])

       searchresult.append(eachresult)

       # print("---------------------------------------------")
    return searchresult



if __name__ == '__main__':
    crawler("我是補路")
