{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":24,"position":24,"stack":[[{"start":{"row":5,"column":7},"end":{"row":5,"column":24},"action":"remove","lines":["requests_oauthlib"],"id":2}],[{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":["r"],"id":3},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["e"]},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":["q"]},{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"insert","lines":["u"]},{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"insert","lines":["e"]}],[{"start":{"row":5,"column":12},"end":{"row":5,"column":13},"action":"insert","lines":["s"],"id":4},{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":["t"]},{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"insert","lines":["s"]},{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"insert","lines":["_"]}],[{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"insert","lines":["o"],"id":5},{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"insert","lines":["a"]},{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":["y"]},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["t"]},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["h"]}],[{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"remove","lines":["h"],"id":6},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"remove","lines":["t"]},{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"remove","lines":["y"]}],[{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":["u"],"id":7},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["t"]},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["h"]},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"insert","lines":["l"]},{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"insert","lines":["i"]},{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"insert","lines":["b"]}],[{"start":{"row":5,"column":24},"end":{"row":5,"column":25},"action":"insert","lines":[" "],"id":8},{"start":{"row":5,"column":25},"end":{"row":6,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":9}],[{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"insert","lines":[","],"id":10}],[{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"insert","lines":[" "],"id":11},{"start":{"row":2,"column":17},"end":{"row":2,"column":18},"action":"insert","lines":["r"]},{"start":{"row":2,"column":18},"end":{"row":2,"column":19},"action":"insert","lines":["e"]}],[{"start":{"row":2,"column":17},"end":{"row":2,"column":19},"action":"remove","lines":["re"],"id":12},{"start":{"row":2,"column":17},"end":{"row":2,"column":34},"action":"insert","lines":["requests_oauthlib"]}],[{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"remove","lines":["import requests_oauthlib ",""],"id":13}],[{"start":{"row":2,"column":17},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":14},{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":["i"]},{"start":{"row":3,"column":1},"end":{"row":3,"column":2},"action":"insert","lines":["m"]}],[{"start":{"row":3,"column":2},"end":{"row":3,"column":3},"action":"insert","lines":["p"],"id":15},{"start":{"row":3,"column":3},"end":{"row":3,"column":4},"action":"insert","lines":["o"]},{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":["r"]},{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":[" "],"id":16}],[{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"remove","lines":[" "],"id":17},{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"remove","lines":[","]}],[{"start":{"row":23,"column":0},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":18}],[{"start":{"row":0,"column":0},"end":{"row":62,"column":5},"action":"remove","lines":["import flask","import os","import requests","import requests_oauthlib","import json","import random","","","app = flask.Flask(__name__)","","","","@app.route('/')","def index():","  ##twitter api...hopefully","    twitt_url = \"https://api.twitter.com/1.1/search/tweets.json?q=kehlanimusic\"","    random_tweet = random.randint(0,14)","    oauth = requests_oauthlib.OAuth1(","    \"eBuX7hYeHDVpIEwgA5cwwAz8P\", ","    \"mEyLbMPJvLS2YAcxFJLk4yT44uhsgLsK5O4kr1w66XwtznEgXv\",","    \"1167289280638726144-s4dO5VvLl5lFvXNMn39aG1vjY2NXuZ\",","    \"ijHOBxlSLDU8jwnLRbMxlCqW6c5FCOkMAQDoqN0MpOvOo\"","    )","","","    ## not sure if this will actually show the tweets, gives links for tweets","    ##a lot of tweets are links...could be a slight issue","    ##max num is 14(15) for tweets","    ","    response = requests.get(twitt_url, auth=oauth)","    json_body = response.json()","    ","    ","    #print(json.dumps(json_body, indent=2))","    ","","    kehlani_tweets = json_body['statuses'][random_tweet]['text']","","    #print(kehlani_tweets)","  ","### genius set up....formatting in index file?    ","    url = \"https://api.genius.com/search?q=Kehlani\"","    ","    ","    my_headers = {","    \"Authorization\": \"Bearer iIUzpgQ_jwrnzWcGPns32mdgaLcLF_KMCZxXydljLb3QLF24GSO1zq38e2uveLY4\"","    }","    ","    playlist = random.randint(0,8)","    response = requests.get(url, headers=my_headers)","    json_body = response.json()","    song = json_body[\"response\"][\"hits\"][playlist][\"result\"][\"full_title\"]","    pic = json_body[\"response\"][\"hits\"][playlist][\"result\"]['header_image_url']","    artist = json_body[\"response\"][\"hits\"][playlist][\"result\"]['primary_artist']['name']","","","    return flask.render_template(\"index.html\", song = song, pic= pic, artist = artist, kehlani_tweets= kehlani_tweets)","","app.run(","        port=int(os.getenv('PORT', 8080)),","        host=os.getenv('IP', '0.0.0.0'),","        debug=True","    )"],"id":19}],[{"start":{"row":0,"column":0},"end":{"row":60,"column":1},"action":"insert","lines":["# app.py","import flask, random, os, requests, json, random, requests_oauthlib  ","","app = flask.Flask(__name__)","","","","@app.route('/')  ","def index(): ","    #Genius API search","    url = \"https://api.genius.com/search?q=Kanye%20West\"","    ","    #Genius API Authorization ","    my_headers = {","    \"Authorization\": \"Bearer IQdtZyfMUnXQ53F8b9e3y-jWqaNNNRXoVK-aUdbF1crCTkG7S_VCvMrMOD_Nm2FR\"","    }","    ","    #Chooses a random song","    random_song = random.randint(0,10)","    response = requests.get(url, headers=my_headers)","    json_body = response.json()","    ","    coverart = json_body[\"response\"][\"hits\"][random_song][\"result\"]['header_image_url']","    song = json_body[\"response\"][\"hits\"][random_song][\"result\"][\"full_title\"]","    artist = json_body[\"response\"][\"hits\"][random_song][\"result\"]['primary_artist']['name']","    ","    ","    #Twitter API to search for tweets","    twitter_url = \"https://api.twitter.com/1.1/search/tweets.json?q=kanyewest\"","    ","    #Retrieves a random tweet","    twitter_tweet = random.randint(0,10)","    ","    #Authorization for the Twitter API","    oauth = requests_oauthlib.OAuth1(","    \"P9G9BJPDMdNWmitx3sn68UXm3\", ","    \"EVTYPFAOVa4jgk9fkYMgTP6dpqwPhniUlht7dLtbORM7Yq9LPr\",","    \"1167117656073412608-vFF34UgaXtFhNDxuXhMceeTadWEL6H\",","    \"90rgA5HLFb4SvWSHEr3q3oRKOnWzPpg4NfSVleWzctQcV\"","    )","","    response = requests.get(twitter_url, auth=oauth)","    json_body = response.json()","    ","","    tweets = json_body['statuses'][twitter_tweet]['text']","  ","    ","","    return flask.render_template(\"index.html\", ","                                coverart = coverart, ","                                song = song, ","                                artist = artist, ","                                tweets = tweets)","","","app.run(","    port=int(os.getenv('PORT', 8080)),","    host=os.getenv('IP', '0.0.0.0'),","    debug = True",")"],"id":20}],[{"start":{"row":10,"column":54},"end":{"row":10,"column":55},"action":"remove","lines":["t"],"id":21},{"start":{"row":10,"column":53},"end":{"row":10,"column":54},"action":"remove","lines":["s"]},{"start":{"row":10,"column":52},"end":{"row":10,"column":53},"action":"remove","lines":["e"]},{"start":{"row":10,"column":51},"end":{"row":10,"column":52},"action":"remove","lines":["W"]},{"start":{"row":10,"column":50},"end":{"row":10,"column":51},"action":"remove","lines":["0"]},{"start":{"row":10,"column":49},"end":{"row":10,"column":50},"action":"remove","lines":["2"]},{"start":{"row":10,"column":48},"end":{"row":10,"column":49},"action":"remove","lines":["%"]},{"start":{"row":10,"column":47},"end":{"row":10,"column":48},"action":"remove","lines":["e"]},{"start":{"row":10,"column":46},"end":{"row":10,"column":47},"action":"remove","lines":["y"]},{"start":{"row":10,"column":45},"end":{"row":10,"column":46},"action":"remove","lines":["n"]},{"start":{"row":10,"column":44},"end":{"row":10,"column":45},"action":"remove","lines":["a"]},{"start":{"row":10,"column":44},"end":{"row":10,"column":45},"action":"insert","lines":["e"]},{"start":{"row":10,"column":45},"end":{"row":10,"column":46},"action":"insert","lines":["h"]},{"start":{"row":10,"column":46},"end":{"row":10,"column":47},"action":"insert","lines":["l"]},{"start":{"row":10,"column":47},"end":{"row":10,"column":48},"action":"insert","lines":["a"]}],[{"start":{"row":10,"column":48},"end":{"row":10,"column":49},"action":"insert","lines":["n"],"id":22},{"start":{"row":10,"column":49},"end":{"row":10,"column":50},"action":"insert","lines":["i"]}],[{"start":{"row":18,"column":36},"end":{"row":18,"column":37},"action":"remove","lines":["0"],"id":23},{"start":{"row":18,"column":35},"end":{"row":18,"column":36},"action":"remove","lines":["1"]}],[{"start":{"row":18,"column":35},"end":{"row":18,"column":36},"action":"insert","lines":["9"],"id":24}],[{"start":{"row":31,"column":38},"end":{"row":31,"column":39},"action":"remove","lines":["0"],"id":25}],[{"start":{"row":31,"column":38},"end":{"row":31,"column":39},"action":"insert","lines":["4"],"id":26}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":60,"column":1},"end":{"row":60,"column":1},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1567796874016,"hash":"eb688c042c2fc9d6ceb0b3235e8bf2a2759ecee6"}