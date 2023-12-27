import requests
from datetime import datetime
import tweepy

# Twitter API credentials
consumer_key = "H9pFvkrsvn9lymBsSwiY2hwMs"
consumer_secret = "hmxSKPKNBkkJX91JPIwx3Drf96SuGy7G4KitcFzGFqzFQsVqLr"
access_token = "1678650680024743936-7GXLS5EOgdh91koLb1EKJ0UAV1EzWo"
access_token_secret = "Qg1OvMOmxYW1CJdvywhPtnHLHvkIeVRb1GhjKhgk2qWcz"

# Function to fetch current public debt transactions
def get_public_debt_transactions():
    api_url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/dts/public_debt_transactions"
    
    # Set the current date
    current_date = datetime.today().strftime('%Y-%m-%d')

    # Set the filter parameter to get data for the current date
    filter_param = f"?filter=record_date:eq:{current_date}"

    # Make a GET request to the API
    response = requests.get(api_url + filter_param)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()

        # Check if the response contains the expected structure and non-empty data
        if 'data' in data and data['data']:
            # Extract the debt transactions data
            return data['data']
        else:
            # Print the response for further analysis
            print("API response does not contain data or data is empty:")
            print(data)
            return None
    else:
        # Handle the case when the request was not successful
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        return None

# Function to post tweet with public debt transactions
def post_tweet(debt_transactions):
    # Twitter authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Compose the tweet
    tweet = f"🇺🇸 U.S. Public Debt Transactions Update 🇺🇸\n\nLatest transactions as of {debt_transactions[0]['record_date']}:\n"

    for transaction in debt_transactions:
        tweet += f"{transaction['transaction_desc']}: ${transaction['transaction_amount']:,.2f}\n"

    tweet += "\n#USDebt #Economy"

    # Post the tweet
    api.update_status(tweet)

# Main function
def main():
    # Get current public debt transactions data
    debt_transactions = get_public_debt_transactions()

    # Check if data is available
    if debt_transactions is not None:
        # Post the tweet
        post_tweet(debt_transactions)
        print("Tweet posted successfully!")
    else:
        print("Tweet not posted due to missing data.")

if __name__ == "__main__":
    main()

