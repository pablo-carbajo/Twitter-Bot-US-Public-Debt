import tweepy
import requests
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver

consumer_key = "H9pFvkrsvn9lymBsSwiY2hwMs"
consumer_secret = "hmxSKPKNBkkJX91JPIwx3Drf96SuGy7G4KitcFzGFqzFQsVqLr"
access_token = "1678650680024743936-7GXLS5EOgdh91koLb1EKJ0UAV1EzWo"
access_token_secret = "Qg1OvMOmxYW1CJdvywhPtnHLHvkIeVRb1GhjKhgk2qWcz"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

import requests
from bs4 import BeautifulSoup

def fetch_debt_data():
    url = "https://www.usdebtclock.org/"

    # Send a GET request to the website
    response = requests.get(url)
    
    if response.status_code == 200:
        # Create a BeautifulSoup object from the HTML content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the elements containing the debt data
        total_debt_element = soup.find(id="national-debt")
        debt_per_capita_element = soup.find(id="us-population")
        debt_gdp_ratio_element = soup.find(id="gdp-amount")

        # Extract the text values from the elements
        total_debt = total_debt_element.get_text().strip()
        debt_per_capita = debt_per_capita_element.get_text().strip()
        debt_gdp_ratio = debt_gdp_ratio_element.get_text().strip()

        debt_data = {
            "total_debt": total_debt,
            "debt_per_capita": debt_per_capita,
            "debt_gdp_ratio": debt_gdp_ratio
        }

        return debt_data
    else:
        # Handle failed request
        print("Failed to fetch U.S. debt data. Status code:", response.status_code)
        return None

def compose_tweet():
    debt_data = fetch_debt_data()

    total_debt = debt_data['total_debt']
    debt_per_capita = debt_data['debt_per_capita']
    debt_gdp_ratio = debt_data['debt_gdp_ratio']

    current_time = datetime.now().strftime("%m/%d/%y %H%M")

    tweet_text = f"{total_debt}$ | {debt_per_capita}$ per citizen | {debt_gdp_ratio}% of the GDP | {current_time} | #USPublicDebt"

    return tweet_text

def post_tweet():
    tweet_text = compose_tweet()
    api.update_status(tweet_text)

post_tweet()



 