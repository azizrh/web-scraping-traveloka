import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import csv
import pandas as pd


# opening url and grabbing the web page
my_url = 'https://www.booking.com/searchresults.html?aid=304142;label=gen173nr-1FCAEoggI46AdIM1gEaGiIAQGYATG4ARfIAQ_YAQHoAQH4AQKIAgGoAgO4ArrwhpEGwAIB0gIkMTE5Njk0NGEtM2YyMS00YmFkLTlmNTMtZTcxNGFjMWYzZDcw2AIF4AIB;sid=f69cca44213bc2d9315e7a7f1c7282a0;checkin=2022-03-04;checkout=2022-03-05;region=5437&'

s=Service(r'C:\Users\62811\Downloads\geckodriver-v0.30.0-win64\geckodriver.exe') 
driver = webdriver.Firefox(service=s)

driver.get(my_url)
time.sleep(10) #experiment with timer to fetch all the data 

# html parsing
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()



name_rating = soup.findAll(True, {'class':['fde444d7ef _c445487e2','af1ddfc958 eba89149fb','_9c5f726ff _192b3a196 f1cbb919ef','_9c5f726ff bd528f9ea6','fde444d7ef _e885fdc12']})
list = []
for nr in name_rating:
    result = nr.text.strip()
    #print(result)
    list.append(nr.text.strip())
name=[]
i=0
while i<len(list):
    name.append(list[i])
    #print(list[i])
    i=i+6

loc=[]
i=1    
while i<len(list):
    #print(list[i])
    loc.append(list[i])
    i=i+6
    
rating=[]
i=3    
while i<len(list):
    #print(list[i])
    rating.append(list[i])
    i=i+6
    
quality=[]
i=4   
while i<len(list):
    #print(list[i])
    quality.append(list[i])
    i=i+6
    
price=[]
i=5   
while i<len(list):
    #print(list[i])
    price.append(list[i])
    i=i+6

df = pd.DataFrame(({'nama': name, 'location': loc,'rating':rating,'quality':quality,'price':price}))
df