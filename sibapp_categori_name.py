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
cat_link_name_list=[]
class GETCATEGORI():
    def __init__ (self,page_link,driver):
        self.page_link =page_link
        self.driver=driver
        ##################################################################################
    def get_cat_link(self):
        cat_link_name_list.clear()
        self.driver.get(self.page_link) 
        

        fb= WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[3]/div/div')))
       
        html=self.driver.execute_script("return arguments[0].outerHTML;",fb)
        page_html_soup=b(html,'html.parser')
        converter = bs2json() 
        # print(page_html_soup)
        class_find_name= page_html_soup.findAll('div',{'class':'MuiGrid-root jss58 MuiGrid-container'}) 
        # # print(class_find_name)        
        json_class_find_name = converter.convertAll(class_find_name)
        print(len(json_class_find_name))
        print(json_class_find_name[0]['div'][1]['div']['div'][1]['a']['div']['div']['p']['text'])
        print(len(json_class_find_name[0]['div']))
        # print(json_class_find_name[0]['div'][0]['div']['div'][1]['a']['div']['div']['p']['text'])
        # print(len(json_class_find_name[0]['div'][0]['div']['div']))
        # print()
        
        categori_app_link=[]
        categori_app_name=[]

        for i in range(1,len(json_class_find_name[0]['div'][0]['div']['div'])):
            categori_app_link.append('https://sibapp.com'+json_class_find_name[0]['div'][0]['div']['div'][i]['a']['attributes']['href'])
            categori_app_name.append(json_class_find_name[0]['div'][0]['div']['div'][i]['a']['div']['div']['p']['text'])
        
        cat_link_name_list.append(categori_app_link)
        cat_link_name_list.append(categori_app_name)
       
        categori_game_link=[]
        categori_game_name=[]
        for i in range(1,len(json_class_find_name[0]['div'][1]['div']['div'])):
            categori_game_link.append('https://sibapp.com'+json_class_find_name[0]['div'][1]['div']['div'][i]['a']['attributes']['href'])
            categori_game_name.append(json_class_find_name[0]['div'][1]['div']['div'][i]['a']['div']['div']['p']['text'])
        
        cat_link_name_list.append(categori_game_link)
        cat_link_name_list.append(categori_game_name)