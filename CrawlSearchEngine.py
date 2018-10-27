import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from collections import OrderedDict
import json
import codecs
import bing , google , yahoo
import re

def crawler(keyword):

    searchEngileList =[google,bing,yahoo]
    searchresult = list()
    hreflist = set()
    repeatlist = list()

    for se in searchEngileList:


        for eachresult in se.crawler(keyword):


            r = re.compile("(?:https?://)?"+eachresult["href"])
            newlist = list(filter(r.match, hreflist))

            if len(newlist) < 1 :

                print(eachresult["title"])
                print(eachresult["href"])
                print(eachresult["brief"])
                print("\n","-----------------------------------\n")

                hreflist.add(eachresult["href"])
                searchresult.append(eachresult)

            else:
                repeatlist.append(eachresult["href"])
                print("repeat se: "+str(se)+eachresult["href"])
        
    print("non repeat: "+str(len(searchresult)))

    for i in repeatlist:
        print(i)
        
    return searchresult



if __name__ == '__main__':

    crawler("蔡孟峰")


    
