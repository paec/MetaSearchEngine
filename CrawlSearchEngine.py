import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from collections import OrderedDict
import json
import codecs
import bing , google


def crawler(keyword):

    searchEngileList =[google,bing]
    searchresult = list()
    hreflist = set()
    repeatlist = list()

    for se in searchEngileList:

        for eachresult in se.crawler(keyword):

            if eachresult["href"] not in hreflist:

                print(eachresult["title"])
                print(eachresult["href"])
                print(eachresult["brief"])
                print("\n","-----------------------------------\n")

                hreflist.add(eachresult["href"])
                searchresult.append(eachresult)

            else:
                repeatlist.append(eachresult["href"])

        
    print(len(searchresult))

    for i in repeatlist:
        print(i)
        
    return searchresult



if __name__ == '__main__':

    crawler("我是補路")


    
