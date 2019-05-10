import itertools
from explicit import waiter, XPATH
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from collections import defaultdict
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import requests
import pandas as pd
from bs4 import BeautifulSoup
from sys import exit
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import shutil
import time 
import random
import re

dataFile = open('charts.txt', 'w')


def scrape_charts_france(number):


    url="https://hypeauditor.com/top-instagram-all-france/?p=%s"%number
    
    # Load page
    driver.get(url)

    # Get the required elements

    accounts=[]
    for elm in driver.find_elements_by_class_name("kyb-ellipsis"):
        
        account=elm.get_attribute("innerHTML")
        account=account[1:]
        
        accounts.append(account)

    return(accounts)

def scrape_charts_world(number):

    url="https://hypeauditor.com/top-instagram/?p=%s"%number
    
    # Load page
    driver.get(url)

    # Get the required elements

    accounts=[]
    for elm in driver.find_elements_by_class_name("kyb-ellipsis"):
        
        account=elm.get_attribute("innerHTML")
        account=account[1:]
        
        accounts.append(account)

    return(accounts)



driver = webdriver.Chrome()    


for page in range(1,21):
    scrape_charts_france(page)
    scrape_charts_world(page)

    for (acc,acc2) in zip(scrape_charts_france(page),scrape_charts_world(page)):
        dataFile.write(str(acc)+'\t'+str(acc2)+'\t')

print('done')
driver.quit()