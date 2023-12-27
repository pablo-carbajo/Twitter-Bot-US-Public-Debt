import requests
import tweepy

# Twitter API credentials
consumer_key = "H9pFvkrsvn9lymBsSwiY2hwMs"
consumer_secret = "hmxSKPKNBkkJX91JPIwx3Drf96SuGy7G4KitcFzGFqzFQsVqLr"
user_id = "1678650680024743936"
user_access_token = "1678650680024743936-7GXLS5EOgdh91koLb1EKJ0UAV1EzWo"
user_access_token_secret = "Qg1OvMOmxYW1CJdvywhPtnHLHvkIeVRb1GhjKhgk2qWcz"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAPLrogEAAAAAENa4QlhaPiLa+qT6TSH/BPqN768=EEYdYMcMvKijMnzvRyLqFqtyV2QS5mOxetLEut3Owyn0Hwgmdt"

# Function to get total public debt amount
def get_total_public_debt_amount():
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
            return data['data'][0]['tot_pub_debt_out_amt']
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
def post_tweet(api, total_public_debt_amount):
    # Convert the total_public_debt_amount to a float
    amount_float = float(total_public_debt_amount)

    # Compose the tweet
    tweet = f"🇺🇸 U.S. Total Public Debt Outstanding Update 🇺🇸\n\nLatest total amount: ${amount_float:,.2f}\n\n#USDebt #Economy"

    # Post the tweet
    api.update_status(tweet)

# Main function
def main():
    # Set up Tweepy with OAuth 1.0a using user-specific credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(user_access_token, user_access_token_secret)
    api = tweepy.API(auth)

    # Post the tweet
    post_tweet(api, get_total_public_debt_amount())
    print("Tweet posted successfully!")

if __name__ == "__main__":
    main()
