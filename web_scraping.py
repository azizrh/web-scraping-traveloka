from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

import bs4
from bs4 import BeautifulSoup

import requests
import pandas as pd
import time
import numpy as np


def append_df_to_excel(df, excel_path):
    df_excel = pd.read_excel(excel_path)
    result = pd.concat([df_excel, df], ignore_index=True)
    result.to_excel(excel_path, index=False)

def strip(x):
    if x !=None:
        return   str(x.text.strip())
    else:
        return str('')


#url link
my_url='https://www.traveloka.com/en-id/'


#calling web driver from its directory
s=Service(r'C:\Users\62811\Downloads\geckodriver-v0.30.0-win64\geckodriver.exe') 

empty_list=[]
a = pd.DataFrame(empty_list,columns= ['name','loc','rating','rating_label','number_of_reviews','price','type','stars_count'])

kota = pd.read_csv(r"Indonesian_Family_Life_Survey_4_Longitude_and_Latitude.csv", usecols=[5,6]).drop_duplicates()

cities=[kota.iloc[102,1],kota.iloc[104,1]]
x=''
for city in cities:
    driver = webdriver.Firefox(service=s)
    wait = WebDriverWait(driver, 30)
    driver.get(my_url)
    search_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='autocomplete-field']"))).send_keys(city)

    #(wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='autocomplete-item-name' and *contains(string(), %s)]"%city)))).click()
    auto_complete = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='autocomplete-item-name'][1]")))
    auto_complete.click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='search-submit-button']"))).click()



    while True:
        try:
            time.sleep(4)
            x = x + wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "_2qd8A"))).get_attribute('innerHTML') #find_elements_by_class_name("_7192d3184")
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"next-button"))).click()
            print("Clicked on  Next Page »")
        except TimeoutException:
            print("No more Next Page »")
            break
    driver.quit()



# empty_list=[]
# a = pd.DataFrame(empty_list,columns= ['name','loc','rating','rating_label','number_of_reviews','price','type','stars_count'])
# a.to_excel("test_web_scraping_py.xlsx")

card=BeautifulSoup(x, 'html.parser').find_all(True,{'class':'ztzlF _2nyWi'})

i=0
list = [ ]
for item in card:

    name = strip(item.find(True, {'class':'_1z5je _10ZQX tvat-hotelName'}))
    
    loc = strip(item.find(True,{'class':'_3tICV'}))
    
    rating = strip(item.find(True,{'class':'tvat-ratingScore'}))

    rating_label_ = ''
    rating_label_ = strip(item.find(True,{'class':'_16hDy'})).split()

    if rating_label_ == []:
        rating_label = ''
    else:
        rating_label = rating_label_[0]
    # except:
    #     rating_label = ''

    number_of_reviews = ''
    number_of_reviews = strip(item.find(True,{'class':'_30os4'}))[1:-1]



    price = strip(item.find(True,{'class':'_22n9I tvat-primaryPrice'}))[3:]
    
    type = strip(item.find(True,{'class':'_3ohst Jewfo _2Vswb'}))
    
    # price_for= strip(item.find(True,{'class':'_4abc4c3d5 _7ee1c7d14'}))

    stars = item.find(True,{'class':'_1RoiH _1dIAz tvat-starRating _1Fq-V'})

    # city = kota.iloc[j,1]

    # province_name = kota.iloc[j,0]

    if stars == None:
        stars_count = ''
    elif len(stars) == 1:
        stars_count = ''
    else:
        stars_count=str(len(stars)-1)

    # href_tag= item.find('a', href=True)['href']

    list_in_list = [name,loc,rating,rating_label,number_of_reviews,price,type,stars_count]#,bed,price_for,stars_count,city,href_tag]
    
    list.append(list_in_list)
    #print(list_in_list)
    i=i+1
df = pd.DataFrame(list,columns= ['name','loc','rating','rating_label','number_of_reviews','price','type','stars_count'])
df.replace('', np.nan, inplace=True)
df.dropna(axis=0,how='all')

append_df_to_excel(df, r"test_web_scraping_py.xlsx")

import winsound
duration = 1000  # milliseconds
freq = 300  # Hz
winsound.Beep(freq, duration)