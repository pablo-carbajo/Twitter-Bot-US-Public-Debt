import requests
from datetime import datetime
import tweepy

# Twitter API credentials
consumer_key = "H9pFvkrsvn9lymBsSwiY2hwMs"
consumer_secret = "hmxSKPKNBkkJX91JPIwx3Drf96SuGy7G4KitcFzGFqzFQsVqLr"
access_token = "1678650680024743936-7GXLS5EOgdh91koLb1EKJ0UAV1EzWo"
access_token_secret = "Qg1OvMOmxYW1CJdvywhPtnHLHvkIeVRb1GhjKhgk2qWcz"

# Function to fetch current total public debt outstanding amount
def get_public_debt_amount():
    endpoint = 'v2/accounting/od/debt_to_penny'
    api_url = f'https://api.fiscaldata.treasury.gov/services/api/fiscal_service/{endpoint}'

    # Make a GET request to the API
    response = requests.get(api_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()

        # Check if the response contains the expected structure and non-empty data
        if 'data' in data and data['data']:
            # Extract the total public debt amount
            return float(data['data'][0]['tot_pub_debt_out_amt'])
        else:
            # Print the response for further analysis
            print("API response does not contain data or data is empty:")
            print(data)
            return None
    else:
        # Handle the case when the request was not successful
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        return None

# Function to post tweet with total public debt amount
def post_tweet(total_public_debt_amount):
    # Twitter authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Compose the tweet
    tweet = f"🇺🇸 U.S. Total Public Debt Outstanding Update 🇺🇸\n\nLatest total amount: ${total_public_debt_amount:,.2f}\n\n#USDebt #Economy"

    # Post the tweet
    api.update_status(tweet)

# Main function
def main():
    # Get current total public debt outstanding amount
    total_public_debt_amount = get_public_debt_amount()

    # Check if data is available
    if total_public_debt_amount is not None:
        # Post the tweet
        post_tweet(total_public_debt_amount)
        print("Tweet posted successfully!")
    else:
        print("Tweet not posted due to missing data.")

if __name__ == "__main__":
    main()

