Flask web application for youtubev3 api  
==========================================

The code attempts to implement Data Mining Lab 1:

> 

List of files
-------------
1. server.py            Backend of app for GET and POST request to serve index.html  
2. index.html           Frontend of app based on bootstrap and jinja2 template  
3. client_secret.json   Authentication information of this application  
4. search.py            Module to get search result using Youtube API  


Usage
==================
To run the application 
    
    python3 server.py
    

    1. Navigate to http://localhost:8090/ and you should see the form staring back at you. 
    2. Enter the search term in search box and click submit
    3. Now results with thumbnails will be displayed. Click on thumbnail to redirect to video.
    4. Click on any of the two button(Name, Published Date) to sort accordingly.I have implemented this type because initially I assumed to sort via 	    buttons. 
    5. Sorting output will be ascending(assumption)  



