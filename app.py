import flask
import os
import requests
import json
import random
import requests_oauthlib

# app = flask.Flask(__name__)


# @app.route('/')
# def index():
  
  
### genius set up....formatting in index file?    
url = "https://api.genius.com/search?q=Kehlani"
    
    
my_headers = {
    "Authorization": "Bearer iIUzpgQ_jwrnzWcGPns32mdgaLcLF_KMCZxXydljLb3QLF24GSO1zq38e2uveLY4"
    }
    
response = requests.get(url, headers=my_headers)
json_body = response.json()
song = json_body["response"]["hits"][0]["result"]["full_title"])
pic = json_body["response"]["hits"][0]["result"]['header_image_url']
artist = json_body["response"]["hits"][0]["result"]['primary_artist']['name']
