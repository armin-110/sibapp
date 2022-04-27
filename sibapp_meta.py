from curses import COLOR_BLACK
from rich import print
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import pandas as pd
import numpy as np
from bs2json import bs2json
import re
import json
import copy
from copy import deepcopy
import requests
from collections import OrderedDict
from iteration_utilities import unique_everseen
import time
import itertools
import schedule
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from sqlalchemy import create_engine
import datetime
import scrapy
meta_list=[]
class Getmeta():
    def __init__ (self,driver,content_link):
        self.driver=driver
        self.content_link=content_link
    def get_meta(self):
        meta_list.clear()
   
        # try:
        try:
            self.driver.get(self.content_link)
            self.driver.refresh()
        except:
            try:
                time.sleep(3)
                self.driver.get(self.content_link)
                self.driver.refresh()
            except:
                time.sleep(3)
                self.driver.get(self.content_link)
                self.driver.refresh()

        converter = bs2json()

        try:
            fb= WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div/div/div[1]')))
        except:
            try:
                self.driver.refresh()
                fb= WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div/div/div[1]')))
            except:
                pass
       
        meta_dic = {'cat':'','categori_name':'','content_name': '','content_link':self.content_link,'rate':'0','ratings':'0','Size':'','Download':'0','Current Version':'','crawling_date':''}
        html=self.driver.execute_script("return arguments[0].outerHTML;",fb)
        html_soup=b(html,'html.parser')
        converter = bs2json()
        class_find=html_soup.findAll('h1',{'class':'jss16'})
        json_class_find = converter.convertAll(class_find)
        # print(json_class_find)
        print(json_class_find[0]['text'])#title
        meta_dic['content_name']=json_class_find[0]['text']
        
        class_find=html_soup.findAll('p',{'class':'jss17'})
        json_class_find= converter.convertAll(class_find)
        pattern = '[,+:ا-ی]'

        # print(json_class_find)   
        try:   
            print(json_class_find[0]['a']['text'])#categori
            meta_dic['categori_name']=json_class_find[0]['a']['text']
        except:
            pass
  
        for i in range(len(json_class_find)):
            if 'دریافت' in json_class_find[i]['text']:
                    
                print(json_class_find[i]['text'])#download
                meta_dic['Download']=int(float(re.sub(pattern,'', json_class_find[i]['text'])))
        
            if 'حجم' in json_class_find[i]['text']:
                print(json_class_find[i]['text'])#size
                meta_dic['Size']=json_class_find[i]['text']
        
            if 'رای ثبت شده' in json_class_find[i]['text']:
                print(json_class_find[i]['text'])#ratings
                meta_dic['ratings']=int(float(re.sub(pattern,'', json_class_find[i]['text'])))
        
        try:

            class_find=html_soup.findAll('p',{'class':'jss21'})
            json_class_find = converter.convertAll(class_find)
            print(json_class_find[0]['text'])#Rate
            meta_dic['rate']=float(json_class_find[0]['text'])
        except:
            pass
        # print(meta_dic)
        meta_list.append(meta_dic)
        # except:
        #     meta_list.append(meta_dic)
