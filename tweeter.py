#!/usr/bin/python
#Packages needed (Debian/Ubuntu): python-tweepy, python-bs4, python-requests

import tweepy
import sys
from bs4 import BeautifulSoup
import requests

def read_tokens(token_file):
	with open(token_file, "r") as f:
		access_token = f.readline()[:-1]
		access_token_secret = f.readline()[:-1]
		api_key = f.readline()[:-1]
		api_secret = f.readline()[:-1]

	return access_token, access_token_secret, api_key, api_secret

def authenticate_and_tweet(message, access_token, access_token_secret, api_key, api_secret):
	auth = tweepy.OAuthHandler(api_key, api_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	api.update_status(message)

def authenticate_and_read(access_token, access_token_secret, api_key, api_secret):
	auth = tweepy.OAuthHandler(api_key, api_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	ipdb.set_trace()

def read_posts(user):
	website = "https://twitter.com/{}".format(user)
	r1 = requests.get(website)
	soup = BeautifulSoup(r1.text)
	for tweet in soup.find_all("p", "ProfileTweet-text js-tweet-text u-dir"):
		print tweet.text
		print ""


#Save access token, access token secret, api key and api secret in a text file called tokens
if __name__ == "__main__":
	if sys.argv[1] == "write":
		tokens = read_tokens("tokens")
		authenticate_and_tweet(" ".join(sys.argv[2:]), *tokens)
	elif sys.argv[1] == "read":
		user = sys.argv[2]
		read_posts(user)


