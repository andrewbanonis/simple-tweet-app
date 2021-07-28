import tweepy

print("Hello there! Welcome to Andrew's scuffed Tweet application! Get started by following the instructions below:")

consumer_key = input("Please enter your twitter consumer key: ")
consumer_secret = input("Please enter your twitter consumer secret key: ")

auth = tweepy.OAuthHandler("API_KEY", "API_SECRET")
auth.set_access_token(consumer_key, consumer_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    authed = True
    print("Authentication OK!")
except:
    authed = False
    print("Authentication FAILED")

tweet = input(str("Please enter the message you would like to tweet: "))


if authed == True:
    api.update_status(tweet)
else:
    print("Tweet failed to send :(, double-check that you used the right consumer tokens.")