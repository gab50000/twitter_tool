#!/usr/bin/python
#Packages needed (Debian/Ubuntu): python-tweepy, python-bs4, python-requests

import tweepy
import sys
from bs4 import BeautifulSoup
import requests
import gnupg
import os

class Twit:

	def __init__(self, token_file):
		self.access_token, self.access_token_secret, self.api_key, self.api_secret = self.read_tokens(token_file)
		auth = tweepy.OAuthHandler(self.api_key, self.api_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)
		self.api = tweepy.API(auth)


	def read_tokens(self, token_file):
		with open(token_file, "r") as f:
			access_token = f.readline()[:-1]
			access_token_secret = f.readline()[:-1]
			api_key = f.readline()[:-1]
			api_secret = f.readline()[:-1]

		return access_token, access_token_secret, api_key, api_secret

	def tweet(self, message):
		self.api.update_status(message)

	def authenticate_and_read(self):
		pass

	def encrypt_and_post(self, text, recipient):
		g = gnupg.GPG()
		possible_matches = []
		for key in g.list_keys():
			if recipient in key["uids"]:
				possible_matches.append(key)
		if len(possible_matches) > 1:
			errormsg = "Recipient name ambiguous. The following keys match the recipient name: \n" + ", ".join([key["uids"] for key in possible_matches])
			raise ValueError(errormsg)
		else:
			fingerprint = possible_matches[0]['fingerprint']
			text_encr = g.encrypt(text, fingerprint)
			#cut encrypted message into tweets of 140 characters length
			delimiters = [(i, min(i+140, len(text_encr.data))) for i in xrange(0, len(text_encr.data), 140)]


def read_posts(user):
	website = "https://twitter.com/{}".format(user)
	r1 = requests.get(website)
	soup = BeautifulSoup(r1.text)
	for tweet in soup.find_all("p", "ProfileTweet-text js-tweet-text u-dir"):
		print tweet.text
		print ""


#Save access token, access token secret, api key and api secret in a text file called tokens
if __name__ == "__main__":
	script_path = os.path.dirname(os.path.realpath(__file__))
	if sys.argv[1] == "write":
		tokens = read_tokens(os.path.join(script_path, "tokens"))
		authenticate_and_tweet(" ".join(sys.argv[2:]), *tokens)
	elif sys.argv[1] == "read":
		user = sys.argv[2]
		read_posts(user)


