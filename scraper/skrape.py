from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


def skrap():
    driver = webdriver.Chrome('chromedriver.exe')
    products = []
    prices = []
    parsed_price = []

    driver.get("https://www.komplett.no/kampanje/121235/nvidia-geforce-3080-3090-3070?q=RTX%2B3080&tag=Vis%20alle")

    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")

    for a in soup.findAll('div', attrs={'class':'product-list-item'}):
        price = a.find('span', attrs={'product-price-now'})
        name = a.find('h2').text

        prices.append(price)
        products.append(name)

    driver.close()

    for i in prices:
        if i is not None:
            j = i.text
            k = " ".join(str(j).split())
            parsed_price.append(str(k))
        else:
            parsed_price.append('not priced yet')

    print('Scraping finished, pushing data to firebase!')

    return parsed_price, products
