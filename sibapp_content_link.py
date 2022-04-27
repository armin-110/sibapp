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
total_link=[]

class Getcontentlinks():
    def __init__ (self,driver,page_link):
        self.driver=driver
        self.page_link=page_link
    def get_link(self):
        
        total_link.clear()

        # try:
        first_page=self.page_link
        while True:
            
            try:
                self.driver.get(first_page)
                self.driver.refresh()
            except:
                try:
                    time.sleep(3)
                    self.driver.get(first_page)
                    self.driver.refresh()
                except:
                    time.sleep(3)
                    self.driver.get(first_page)
                    self.driver.refresh()

            converter = bs2json()
        
            try:
                self.driver.refresh()
                fb= WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div/div/div')))
            except:
                try:
                    self.driver.refresh()
                    fb= WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div/div/div')))
                except:
                    try:
                        self.driver.refresh()
                        fb= WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div/div/div')))
                    except:
                        pass
            try:
                html=self.driver.execute_script("return arguments[0].outerHTML;",fb)
                html_soup=b(html,'html.parser')
                converter = bs2json()
                            
                            
                class_find=html_soup.findAll('div',{'class':'MuiGrid-root jss59 MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-6 MuiGrid-grid-md-4'})
                json_class_find = converter.convertAll(class_find)
                # # print(json_class_find[12])
                for i in range(len(json_class_find)):
                    total_link.append('https://sibapp.com'+json_class_find[i]['a']['attributes']['href'])
                    # print(json_class_find[i]['a']['attributes']['href'])
                    # print(json_class_find[i]['a']['div']['div'][1]['p'][0]['text'])
            
                # try:
                class_find=html_soup.findAll('div',{'class':'MuiGrid-root jss58 MuiGrid-container MuiGrid-justify-content-xs-center'})
                json_class_find = converter.convertAll(class_find)
                print(json_class_find)
                print(len(json_class_find))

                if len(json_class_find)==0:
                    print('please break')
                    break
                if len(json_class_find)==1:
                    try:
                        print('salam bar hossein')
                        if json_class_find[0]['a']['div']['text']=='صفحه بعدی':
                            print(json_class_find[0]['a']['div']['text'])
                            print(json_class_find[0]['a']['attributes']['href'])
                            new_page=json_class_find[0]['a']['attributes']['href']
                            first_page='https://sibapp.com'+new_page
                        else:
                        # print('please break')  
                            break  
                    except:
                        print('please break')  
                        break
                if len(json_class_find)>1:
                    print('salam bar hasan')
                    print(json_class_find[1]['a']['attributes']['href'])
                    print(json_class_find[1]['a']['div']['text'])
                    new_page=json_class_find[1]['a']['attributes']['href']
                    first_page='https://sibapp.com'+new_page
                time.sleep(2)
            except:
                print('page not loaded')    
           
         