# hcjson2humanreadable


Just a quick one-off py script to format json file from Hipchat logs/history to stdout in a human readable format.


## Requirements: 

- You need Python 3. ***  Does not work with Python2.
- You need the json file from Hipchat to parse.


## Quick instructions: 

1. Get your json file either from hipchat support or from the Hipchat RESTful API.  See https://www.hipchat.com/docs/apiv2 and https://developer.atlassian.com/server/hipchat/about-the-hipchat-rest-api/ for more information, if needed. 

2. Put this script file in the same directory. 

3. Run the script.  (It will ask you which *.json file would you like to parse.) 


## Notes: 

This script is able to parse: 
 
* 1-on-1 chat histories 
* Room chat histories
* URL's posted in messages
* File attachments posted in messages
* Messages deleted by a Hipchat administrator

 

Additionally, it is also able to deal with "administratively deleted" messages. 


## Possible Future Work (?): 

- Python2 compatibility.
- Output to CSV, not just stdout. 
- Parse multiple files at a time. 
- Do webrequests to retrieve chat history files from Hipchat API.	
- Convert date/time format from Zulu to local (ET).


