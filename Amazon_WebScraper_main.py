import ssl

from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
sender = "mjcolon218@gmail.com"
receiver = ["mjcolom218@gmail.com"]
message = """Whats up bro
"""
url = "https://www.amazon.com/Instant-Pot-60-Max-Electric/dp/B077T9YGRM/ref=dp_fod_2?pd_rd_i=B077T9YGRM&psc=1"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",
           "Accept-Language":"en-us"}


response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.content,"lxml")
#print(soup.prettify())
price = soup.find("span",class_="a-size-medium a-color-price").getText()
print(price)
price_split = float(price.split("$")[1])
print(price_split)
buy_price = 200
message_2 = f"hi moe, the price is $ {price_split}"
me = "mjcolon218@yahoo.com"
my_password = "*********"
moe = "mjcolon218@gmail.com"
port = 465
if price_split < buy_price:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",port, context=context) as server:
        server.login("mjcolon218@gmail.com",my_password)
        server.sendmail(moe,me,message_2)
