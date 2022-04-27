print('بسمه الله الرحمن الرحیم')
print('salam bar mohammadreza dehghan amiri')
import datetime
from sqlalchemy import create_engine
import schedule
import itertools
import time
from iteration_utilities import unique_everseen
from collections import OrderedDict
import requests
from copy import deepcopy
import copy
import json
import re
from bs2json import bs2json
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as b
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from rich import print
from curses import COLOR_BLACK

import sibapp_categori_name
import sibapp_content_link
import sibapp_meta

def get_cat_link_name(page_link):
    driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
    sg = sibapp_categori_name.GETCATEGORI(page_link, driver)
    sgg = sg.get_cat_link()
    driver.close()
    return(sibapp_categori_name.cat_link_name_list)    


def get_page_links(page_link):
    driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
    gf = sibapp_content_link.Getcontentlinks(driver, page_link)
    gf.get_link()
    driver.close()
    return (sibapp_content_link.total_link)

def get_metadata(content_link):
    driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
    gf = sibapp_meta.Getmeta(driver, content_link)
    gf.get_meta()
    driver.close()
    return (sibapp_meta.meta_list)
###################################################################################
date_a=datetime.datetime.now()
engine = create_engine('postgresql://postgres:12344321@10.32.141.17/sibapp',pool_size=20, max_overflow=100,)
con=engine.connect()

cat=get_cat_link_name('https://sibapp.com/categories') 
program_link=cat[0]
program_name=cat[1]
game_link=cat[2]
game_name=cat[3]


# page_link=get_page_links('https://sibapp.com/categories/jzQhWNxA?page=1')
# page_link=get_page_links('https://sibapp.com/categories/itunes_Education?page=1')
# page_link=get_page_links('https://sibapp.com/categories/EL39bBnM?page=1')


# link_meta=get_metadata('https://sibapp.com/applications/suret?from=category')
# print(link_meta)

for i in range(len(program_link)):
    page_link=get_page_links(program_link[i])
    for j in range(len(page_link)):
        link_meta=get_metadata(page_link[j])
        # print(link_meta[0])
        date_i=datetime.datetime.now()
        link_meta[0]['crawling_date']=str(date_i.date()).replace('-','')+str(date_i.time()).split(':')[0]
        # link_meta[0]['categori_name']=program_name[j]
        link_meta[0]['cat']='program'
        data_frame =pd.DataFrame(link_meta[0],index=[0])
        data_frame.to_sql('sibapp_meta'+str(date_a.date()).replace('-','')+str(date_a.time()).split(':')[0],con,if_exists='append', index=False)
        print(link_meta[0])

for i in range(len(game_link)):
    page_link=get_page_links(game_link[i])
    for j in range(len(page_link)):
        link_meta=get_metadata(page_link[j])
        # print(link_meta[0])
        date_i=datetime.datetime.now()
        link_meta[0]['crawling_date']=str(date_i.date()).replace('-','')+str(date_i.time()).split(':')[0]
        # link_meta[0]['categori_name']=program_name[j]
        link_meta[0]['cat']='game'
        data_frame =pd.DataFrame(link_meta[0],index=[0])
        data_frame.to_sql('sibapp_meta'+str(date_a.date()).replace('-','')+str(date_a.time()).split(':')[0],con,if_exists='append', index=False)
        print(link_meta[0])

