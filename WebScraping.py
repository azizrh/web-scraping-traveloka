import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

my_url = 'https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaGiIAQGYATG4ARfIAQ_YAQHoAQH4AQKIAgGoAgO4ArrwhpEGwAIB0gIkMTE5Njk0NGEtM2YyMS00YmFkLTlmNTMtZTcxNGFjMWYzZDcw2AIF4AIB&sid=f69cca44213bc2d9315e7a7f1c7282a0&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.html%3Flabel%3Dgen173nr-1FCAEoggI46AdIM1gEaGiIAQGYATG4ARfIAQ_YAQHoAQH4AQKIAgGoAgO4ArrwhpEGwAIB0gIkMTE5Njk0NGEtM2YyMS00YmFkLTlmNTMtZTcxNGFjMWYzZDcw2AIF4AIB%3Bsid%3Df69cca44213bc2d9315e7a7f1c7282a0%3Bsb_price_type%3Dtotal%26%3B&ss=Jakarta%2C+Jakarta+Province%2C+Indonesia&is_ski_area=0&checkin_year=2022&checkin_month=3&checkin_monthday=4&checkout_year=2022&checkout_month=3&checkout_monthday=5&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ac_position=0&ac_langcode=en&ac_click_type=b&dest_id=-2679652&dest_type=city&iata=JKT&place_id_lat=-6.194998&place_id_lon=106.82294&search_pageview_id=8d1130dd0bd30184&search_selected=true&ss_raw=jakarta'# 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

# opening url and grabbing the web page
uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, 'html.parser')
print(page_soup.prettify())

# grabbing all containers with class name = item-container
# containers = page_soup.findAll('div', {'class':'item-container'})

# filename = "products.csv"
# f = open(filename, 'w')

# headers = "brands, product_name, shipping\n"

# f.write(headers)

# container = containers[1]

# for container in containers:
#     brand = container.div.div.a.img['title']
#     title_container = container.findAll('a', {'class':'item-title'})
#     product_name = title_container[0].text
#     ship_container = container.findAll('li', {'class':'price-ship'})
#     # use strip() to remove blank spaces before and after text
#     shipping = ship_container[0].text.strip()

#     print("brand:" + brand)
#     print("product_name:" + product_name)
#     print("shipping:" + shipping)

#     f.write(brand + ',' + product_name.replace(',' , '|') + ',' + shipping + '\n')

# f.close()

