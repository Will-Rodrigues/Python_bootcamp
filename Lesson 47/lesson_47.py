import requests
from bs4 import BeautifulSoup
import lxml
import smtplib as smtp

EMAIL = ''
PASS = ''

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get('https://www.amazon.com.br/Redragon-TECLADO-MECANICO-RAINBOW-BRANCO/dp/B09YMTQ6Y7/ref=sr_1_11?keywords=teclado+mecanico&qid=1658784868&s=computers&sprefix=teclado%2Ccomputers%2C234&sr=1-11&ufe=app_do%3Aamzn1.fos.fcd6d665-32ba-4479-9f21-b774e276a678', headers=header)

item_html = response.text
soup = BeautifulSoup(item_html, "lxml")
price = soup.find(class_="a-offscreen").getText()
no_symbol_price = price.replace("R$", '')
float_price = float(no_symbol_price.replace(',', '.'))

if float_price < 170.00:
    with smtp.SMTP("smtp.office365.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASS)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject: Your product is lower\n\nThe new price of the product is {float_price}")
