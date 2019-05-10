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

dataFile = open('liste_users1.txt', 'w')


# Get the number of following users of the account

def get_following_number(username):
    url = "https://www.instagram.com/%s/"%username

    response = Request(url)
    try:
        html = urlopen(response).read()
    except HTTPError:
        return 0
    fancyHTML = BeautifulSoup(html, "html.parser")

    metaContentTags = fancyHTML.select("meta[content]")
    follower = 0
    tags=metaContentTags[15]

    strContent = tags.get("content").replace(",", "")
    
    result = (re.findall(r'([+-]?\d*\.?\d+k*)', strContent)[0])

    strContent=strContent[:20]

    Million=False
    if 'm' in strContent[:20]:
        Million=True

    if Million==True:
        result=result+'m'

    if result[-1] == "k":
        if result.split(".")[0] == result:
            follower=int(result.strip("k"))*1000
        else:
            follower=int(result.split(".")[0])*1000+int(result.split(".")[1].strip("k"))*100
    elif result[-1]== "m":
        if result.split(".")[0]== result:
            follower=int(result.strip("m"))*1000000
        else:
            follower=int(result.split(".")[0])*1000000+int(result.split(".")[1].strip("m"))*1000
    else:
        follower=int(result)
    return(follower)


# Login to instagram with a ghost account to scrape users pages

def login(driver):
    username = ""  # <username here>
    password = ""  # <password here>

    # Load page
    driver.get("https://www.instagram.com/accounts/login/")

    # Login
    waiter.find_write(driver, "//div/input[@name='username']", username, by=XPATH)
    waiter.find_write(driver, "//div/input[@name='password']", password, by=XPATH)
    waiter.find_element(driver, "//div/button[@type='submit']", by=XPATH).click()

    # Click on disable notifications
    ui.WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()


#check if the account is private

def private(driver, account):
    driver.get("https://www.instagram.com/{0}/".format(account))
    if len(driver.find_elements_by_xpath("//div[@class='Nd_Rl _2z6nI']"))==0:
        return(False)
    else:
        return(True)

    

#get the following usernames of the account

def scrape_following(driver, account):
    # Load account page
   
    driver.get("https://www.instagram.com/{0}/".format(account))

    # Click the 'Follower(s)' link
    try:
        driver.find_element_by_partial_link_text("abonnés").click()
    
        # Wait for the followers modal to load
        waiter.find_element(driver, "//div[@role='dialog']", by=XPATH)

        # get the number of following

        allfoll=int(get_following_number(account))
        allfoll=int(allfoll/4)

        # if the number of following is too high (approx more than 1,000), we won't go through the whole list (too long)
        iteration=500
    
        # now scroll. If a problem occurds, should automatically correct it
        for j in range(iteration):
            driver.execute_script('''
            var fDialog = document.querySelector('div[role="dialog"] .isgrP');
            fDialog.scrollTop = fDialog.scrollTop+600
            ''')
            
            if len(driver.find_elements_by_xpath('//div[@class="_7UhW9  PIoXz       MMzan   _0PwGv           fDxYl     "]'))!=0:
                driver.execute_script('''
                var fDialog = document.querySelector('div[role="dialog"] .isgrP');
                fDialog.scrollTop = fDialog.scrollTop-300
                ''')
                time.sleep(3)
                driver.execute_script('''
                var fDialog = document.querySelector('div[role="dialog"] .isgrP');
                fDialog.scrollTop = fDialog.scrollTop-400
                ''')

            time.sleep(random.randint(500,1000)/1000)
            print("Extract followers %",round((j/(iteration)*100),2),"from","%100")
            
        following=[]
        print('exporting...')
        for elm in driver.find_elements_by_xpath("//a[@class='FPmhX notranslate _0imsa ']"):
            following.append(elm.get_attribute("title"))

    except:
        following=['']
        
    return(following)



#charger la liste d'influenceurs
users=['coline','lilibarbery','deedeeparis','bestofvanity','mangoandsalt']



driver = webdriver.Chrome()


#Remove private users from initial list
public_users=[usr for usr in users if private(driver,str(usr))==False]


login(driver)

for usr in public_users:
    account = str(usr)
    print('user proceeded:',usr)
    dataFile.write(str(usr)+'\t')
    for fol in scrape_following(driver, account):
        dataFile.write(str(fol)+'\t')

    dataFile.write('\n')

driver.quit()
