### Web scraper that takes prices of the new RTX GPUs from www.komplett.no
### and pushes the information to firebase.
from db.user import User
from scraper.skrape import skrap
import datetime


user = User('william')  # User login
prices, models = skrap()  # Scrape komplett RTX 30-series site

print()

for i in range(166): # TODO: fix so its dynamic
    user.append_data(models[i], prices[i])  # push data to firebase

