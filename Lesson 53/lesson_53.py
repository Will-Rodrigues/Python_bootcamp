from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import requests
import time

SERVICE = Service('C:\Development\chromedriver.exe')
FORM_URI = 'https://docs.google.com/forms/d/e/1FAIpQLScTNKZ86QPKs_7l65w-xqifeVhPwGdzOL8KsoMd4KEbO4yAOQ/viewform?usp=sf_link'

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get("https://www.zillow.com/portland-or/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Portland%2C%20OR%22%2C%22mapBounds%22%3A%7B%22west%22%3A-123.1186676328125%2C%22east%22%3A-122.2727203671875%2C%22south%22%3A45.30193868332958%2C%22north%22%3A45.80774281330017%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A13373%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A456256%7D%2C%22mp%22%3A%7B%22max%22%3A2000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D", headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")
all_link_elements = soup.select(".list-card-top a")

all_links = []
for link in all_link_elements:
    href = link["href"]
    print(href)
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

all_address_elements = soup.select(".list-card-info address")
all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]

all_price_elements = soup.select(".list-card-heading")
all_prices = []
for element in all_price_elements:
    try:
        price = element.select(".list-card-price")[0].contents[0]
    except IndexError:
        print('Multiple listings for the card')
        price = element.select(".list-card-details li")[0].contents[0]
    finally:
        all_prices.append(price)

driver = webdriver.Chrome(service=SERVICE)

for n in range(len(all_links)):
    driver.get(FORM_URI)

    time.sleep(2)
    address = driver.find_element(By.XPATH, 
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH, 
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH, 
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()
