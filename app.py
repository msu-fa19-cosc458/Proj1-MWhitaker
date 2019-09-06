import flask
import os
import requests
import requests_oauthlib
import json
import random


app = flask.Flask(__name__)



@app.route('/')
def index():
  ##twitter api...hopefully
    twitt_url = "https://api.twitter.com/1.1/search/tweets.json?q=kehlanimusic"
    random_tweet = random.randint(0,14)
    oauth = requests_oauthlib.OAuth1(
    "eBuX7hYeHDVpIEwgA5cwwAz8P", 
    "mEyLbMPJvLS2YAcxFJLk4yT44uhsgLsK5O4kr1w66XwtznEgXv",
    "1167289280638726144-s4dO5VvLl5lFvXNMn39aG1vjY2NXuZ",
    "ijHOBxlSLDU8jwnLRbMxlCqW6c5FCOkMAQDoqN0MpOvOo"
    )

    ## not sure if this will actually show the tweets, gives links for tweets
    ##a lot of tweets are links...could be a slight issue
    ##max num is 14(15) for tweets
    
    response = requests.get(twitt_url, auth=oauth)
    json_body = response.json()
    
    
    #print(json.dumps(json_body, indent=2))
    

    kehlani_tweets = json_body['statuses'][random_tweet]['text']

    #print(kehlani_tweets)
  
### genius set up....formatting in index file?    
    url = "https://api.genius.com/search?q=Kehlani"
    
    
    my_headers = {
    "Authorization": "Bearer iIUzpgQ_jwrnzWcGPns32mdgaLcLF_KMCZxXydljLb3QLF24GSO1zq38e2uveLY4"
    }
    
    playlist = random.randint(0,8)
    response = requests.get(url, headers=my_headers)
    json_body = response.json()
    song = json_body["response"]["hits"][playlist]["result"]["full_title"]
    pic = json_body["response"]["hits"][playlist]["result"]['header_image_url']
    artist = json_body["response"]["hits"][playlist]["result"]['primary_artist']['name']


    return flask.render_template("index.html", song = song, pic= pic, artist = artist, kehlani_tweets= kehlani_tweets)

app.run(
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0'),
        debug=True
    )