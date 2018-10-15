# hcjson2humanreadable


Just a quick one-off py script to format json file from Hipchat logs/history to stdout in a human readable format.


## Quick instructions: 

1. Get your json file either from hipchat support or from the Hipchat RESTful API.  See https://www.hipchat.com/docs/apiv2 and https://developer.atlassian.com/server/hipchat/about-the-hipchat-rest-api/ for more information, if needed. 

2. Put this script file in the same directory as your *.json export. 

3. Run the script.  It will ask you which *.json file would you like to parse. 


## Notes: 

This script seems to work with both 1-on-1 chat histories, as well as Room chats. 

Additionally, it is also able to deal with "administratively deleted" messages. 


## Possible Future Work (?): 

i.	Only sending to stdout - but maybe will spend time outputting to csv at some point. 
ii.	Only parsing one file at a time. 


