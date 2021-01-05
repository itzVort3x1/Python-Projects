import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "<From mail address>"
MY_PASSWORD = "<Password of the mail address>"

product_url = "<Product link to be checked>"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(product_url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
# print(soup.prettify())

price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("₹")[1]
formatted_currency = price_without_currency.replace(',', "")
price_as_float = float(formatted_currency)
if price_as_float < 2000.0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="<to mail address>", msg=f"Subject: LOW PRICE!\n\nPrice of the product is {price_as_float}\n click the link below to buy! \n{product_url}")
