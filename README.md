# hcjson2humanreadable


Just a quick one-off py script to format json file from Hipchat logs/history to stdout in a human readable format.


## Requirements: 

- Python 3. ***  Does not work with Python2.
- The json file from Hipchat to parse.


## Quick instructions: 

1. Get your json file either from hipchat support or from the Hipchat RESTful API.  See https://www.hipchat.com/docs/apiv2 and https://developer.atlassian.com/server/hipchat/about-the-hipchat-rest-api/ for more information, if needed. 

2. Put this script file in the same directory as your *.json export. 

3. Run the script.  It will ask you which *.json file would you like to parse. 


## Notes: 

This script seems to work with both 1-on-1 chat histories, as well as Room chats. 

Additionally, it is also able to deal with "administratively deleted" messages. 


## Possible Future Work (?): 

- Output to CSV, not just stdout. 
- Parse multiple files at a time. 
- Do webrequests to retrieve chat history files from Hipchat API.	


