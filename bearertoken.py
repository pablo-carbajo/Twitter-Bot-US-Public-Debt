import requests
import base64

def get_bearer_token(consumer_key, consumer_secret):
    # Twitter API endpoint for obtaining bearer token
    token_url = "https://api.twitter.com/oauth2/token"

    # Concatenate the consumer key and secret for authentication
    credentials = f"{consumer_key}:{consumer_secret}"

    # Base64 encode the credentials
    encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")

    # Set headers for the request
    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    }

    # Data for the request payload
    data = {"grant_type": "client_credentials"}

    # Make a POST request to obtain the bearer token
    response = requests.post(token_url, headers=headers, data=data)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        token_data = response.json()
        # Extract and return the bearer token
        return token_data.get("access_token")
    else:
        # Print the error details if the request was not successful
        print(f"Error getting bearer token. Status code: {response.status_code}")
        print(response.text)
        return None

# Replace with your actual consumer key and secret
consumer_key = "H9pFvkrsvn9lymBsSwiY2hwMs"
consumer_secret = "hmxSKPKNBkkJX91JPIwx3Drf96SuGy7G4KitcFzGFqzFQsVqLr"

# Get the bearer token
bearer_token = get_bearer_token(consumer_key, consumer_secret)

# Check if the bearer token is obtained successfully
if bearer_token:
    print(f"Bearer Token: {bearer_token}")
else:
    print("Bearer token retrieval failed.")
