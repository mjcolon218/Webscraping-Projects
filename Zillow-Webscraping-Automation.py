
# ***************************************** ---------- Importing-***** - *****-Libraries ---------- ********************************************** #

from bs4 import BeautifulSoup
import requests
import lxml
from selenium import webdriver
import time




headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",
           "Accept-Language":"en-us"}

URl =  "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.49395370483398%2C%22east%22%3A-122.34134674072266%2C%22south%22%3A37.73732676207093%2C%22north%22%3A37.81561543127037%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D"
response = requests.get(URl, headers=headers)
real_estate_data = response.text
soup = BeautifulSoup(real_estate_data, "html.parser")
all_html_elements = soup.select(".list-card-info a")
all_links = []
for link in all_html_elements:
    href = link['href']
    if "https" not in href:
        all_links.append(f'http://www.zillow.com{href}')

    else:
        all_links.append(href)


all_addresses_elements = soup.select(".list-card-info address")
all_address = [address.getText().split('|')[-1] for address in all_addresses_elements]

all_prices = []
all_price_elements = soup.select(".list-card-heading")
for price in all_price_elements:
    try:
        prices =price.select(".list-card-price")[0].contents[0].split('/')[0]

    except IndexError:

        prices = price.select(".list-card-details li")



    finally:
        all_prices.append(prices)



chrome_driver_path = "/Users/madisonavemoe/Desktop/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()
for n in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdqdOcwKJG_E05H3GmYUUTtTBvzyeaCPQ18kfJnEt8FxUGjYw/viewform?usp=sf_link")
    time.sleep(2)
    address_q = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    ppm_q = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    http_q = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    address_q.send_keys(all_address[n])
    ppm_q.send_keys(all_prices[n])
    http_q.send_keys(all_links[n])
    driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span").click()
