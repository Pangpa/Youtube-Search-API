## ![](http://www.google.com/images/icons/product/youtube-32.png) YouTube Search API

Flask web application for [Youtube APIv3](https://developers.google.com/youtube/v3/getting-started)  
==========================================

> Youtube API v3 implementation using [flask](http://flask.pocoo.org/) web app and [jinja2](http://jinja.pocoo.org/docs/2.10/) template.


### List of files

* server.py            Backend of app for GET and POST request to serve index.html  
* index.html           Frontend of app based on bootstrap and jinja2 template  
* client_secret.json   Authentication information of this application  
* search.py            Module to get search result using Youtube API  


## Getting Started

### Prerequisites

*  Linux operating system with `pip3` and `python3` installed.
* `flask` should be installed
* `wtforms` should be installed
* `argparse` should be installed
* `json` should be installed
* pip3 install `operator`
* pip3 install --upgrade google-api-python-client
* pip3 install --upgrade google-auth google-auth-oauthlib google-auth-httplib2

### Usage

### To run the application 
    
  
 #### 1. Start the server:
 ```shell
 python3 server.py
```
 #### 2. Launch the web app:
 
Navigate to  http://localhost:8090 to launch app. 


Enter the search term in search box and click submit.Now results with thumbnails will be displayed. Click on thumbnail to redirect to video. 

Click on any of the two button (Name, Published Date) to sort accordingly because It is  assumed to sort via buttons. Sorting output will be by default ascending.
