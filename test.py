import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import csv
import pandas as pd


my_url = 'https://www.booking.com/searchresults.html?aid=304142;label=gen173nr-1FCAEoggI46AdIM1gEaGiIAQGYATG4ARfIAQ_YAQHoAQH4AQKIAgGoAgO4ArrwhpEGwAIB0gIkMTE5Njk0NGEtM2YyMS00YmFkLTlmNTMtZTcxNGFjMWYzZDcw2AIF4AIB;sid=f69cca44213bc2d9315e7a7f1c7282a0;checkin=2022-03-04;checkout=2022-03-05;region=5437&'

#'https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaGiIAQGYATG4ARfIAQ_YAQHoAQH4AQKIAgGoAgO4ArrwhpEGwAIB0gIkMTE5Njk0NGEtM2YyMS00YmFkLTlmNTMtZTcxNGFjMWYzZDcw2AIF4AIB&sid=f69cca44213bc2d9315e7a7f1c7282a0&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.html%3Flabel%3Dgen173nr-1FCAEoggI46AdIM1gEaGiIAQGYATG4ARfIAQ_YAQHoAQH4AQKIAgGoAgO4ArrwhpEGwAIB0gIkMTE5Njk0NGEtM2YyMS00YmFkLTlmNTMtZTcxNGFjMWYzZDcw2AIF4AIB%3Bsid%3Df69cca44213bc2d9315e7a7f1c7282a0%3Bsb_price_type%3Dtotal%26%3B&ss=Jakarta%2C+Jakarta+Province%2C+Indonesia&is_ski_area=0&checkin_year=2022&checkin_month=3&checkin_monthday=4&checkout_year=2022&checkout_month=3&checkout_monthday=5&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ac_position=0&ac_langcode=en&ac_click_type=b&dest_id=-2679652&dest_type=city&iata=JKT&place_id_lat=-6.194998&place_id_lon=106.82294&search_pageview_id=8d1130dd0bd30184&search_selected=true&ss_raw=jakarta'

#'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

# opening url and grabbing the web page
# uClient = urlopen(my_url)
# page_html = uClient.read()
# uClient.close()

# s=Service(r'C:\Users\62811\Documents\chromedriver_win32\chromedriver.exe') 
# driver = webdriver.Chrome(service=s)
s=Service(r'C:\Users\62811\Downloads\geckodriver-v0.30.0-win64\geckodriver.exe') 
driver = webdriver.Firefox(service=s)


driver.get(my_url)
time.sleep(10) #experiment with timer to fetch all the data 



# html parsing
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()
#page_soup = soup(page_html, 'html.parser')
#pretty_soup = print(soup.prettify())
pretty_soup = soup.prettify()

# f = open("test_scrapping.html", "x")
# f.write(str(pretty_soup))
# f.close()

# grabbing all containers with class name = item-container
containers = soup.findAll('div', {'class':'fde444d7ef _c445487e2'})
ratings = soup.findAll('div',{'class':'_9c5f726ff bd528f9ea6'})
#print(containers)

#print nama2 hotel


name = []
for name_box in containers:
    names = name_box.text.strip() #remove starting and trailing
    name.append(str(names))
    #print(name)
rating = []
for rating_box in ratings:
    ratings = rating_box.text.strip() #remove starting and trailing
    rating.append(ratings)
    #print(rating)

# #write into csv-file
# with open('test.csv', 'a') as csv_file:
#    writer = csv.writer(csv_file)
#    writer.writerow([name, rating])

# df = pd.DataFrame([({'nama': name, 'rating': rating})])
# df

name_rating = soup.findAll(True, {'class':['fde444d7ef _c445487e2','_9c5f726ff bd528f9ea6']})
for nr in name_rating:
    print(nr.text.strip())
