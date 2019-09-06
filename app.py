import flask
import os
import requests
import json
import random
import requests_oauthlib

# app = flask.Flask(__name__)


# @app.route('/')
# def index():
  
  
##twitter api...hopefully


twitt_url = "https://api.twitter.com/1.1/search/tweets.json?q=kehlanimusic"

oauth = requests_oauthlib.OAuth1(
    "eBuX7hYeHDVpIEwgA5cwwAz8P", 
    "mEyLbMPJvLS2YAcxFJLk4yT44uhsgLsK5O4kr1w66XwtznEgXv",
    "1167289280638726144-s4dO5VvLl5lFvXNMn39aG1vjY2NXuZ",
    "ijHOBxlSLDU8jwnLRbMxlCqW6c5FCOkMAQDoqN0MpOvOo"
)
## not sure if this will actually show the tweets, gives links for tweets
response = requests.get(twitt_url, auth=oauth)
json_body = response.json()
#print(json.dumps(json_body, indent=2))

tweetfeed = json_body['statuses'][14]['text']

print(tweetfeed)
  
### genius set up....formatting in index file?    
url = "https://api.genius.com/search?q=Kehlani"
    
    
my_headers = {
    "Authorization": "Bearer iIUzpgQ_jwrnzWcGPns32mdgaLcLF_KMCZxXydljLb3QLF24GSO1zq38e2uveLY4"
    }
    
response = requests.get(url, headers=my_headers)
json_body = response.json()
song = json_body["response"]["hits"][0]["result"]["full_title"]
pic = json_body["response"]["hits"][0]["result"]['header_image_url']
artist = json_body["response"]["hits"][0]["result"]['primary_artist']['name']
