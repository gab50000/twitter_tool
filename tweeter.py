#!/usr/bin/python

import tweepy
import sys
import ipdb

def read_tokens(token_file):
	with open(token_file, "r") as f:
		

def authenticate_and_tweet(message):
	auth = tweepy.OAuthHandler(api_key, api_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	api.update_status(message)

def authenticate_and_read():
	auth = tweepy.OAuthHandler(api_key, api_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	ipdb.set_trace()

if __name__ == "__main__":
	if sys.argv[1] == "write":
		authenticate_and_tweet(" ".join(sys.argv[2:]))
	elif sys.argv[1] == "read":
		authenticate_and_read()


