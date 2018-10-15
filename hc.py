# Run this python script, then make sure the Hipchat json file is in the same directory.

import json, os, fnmatch

# Print out what the current directory is, and
# request input of what json file to work with:
cwd = os.getcwd()
print("Your current directory is:", cwd)
print("Below are the *.json files:")
listofJson = os.listdir('.')
pattern = "*.json"
for entry in listofJson:
     if fnmatch.fnmatch(entry, pattern):
             print (entry)

_jsonfile = input("Input the filename to work with: ")
with open(_jsonfile) as f:
    data = json.load(f)

# To view the raw json cleaned-up so that it can make sense:
# print(json.dumps(data, indent=3))
#
# OPTIONAL
# print(type(data)
# response: <class 'dict'>
# print(type(data['items']))
# response: <class 'list'>
# Show how many objects/dictionaries in 'items'
print ("There are", len(data['items']), "messages in this file.")

# Get typical values (date/timestamp, who or where the msg is from, and the message itself)
# in human readable format...
for msg in data['items']:
    if msg['message'] == None:
        #print("........... THIS IS A DELETED MESSAGE.........")
        mention_name = msg['from']['mention_name']
        name = msg['from']['name']
        print(msg['date'], "\t" + mention_name, "\t" + name, "\t" + "THIS IS A DELETED MESSAGE.")
    elif msg['message'] != None and msg['type'] == 'message':
        #        print("This is a normal message")
        mention_name = msg['from']['mention_name']
        name = msg['from']['name']
        print(msg['date'], "\t" + mention_name, "\t" + name, "\t" + msg['message'])
    elif msg['type'] == 'notification':
        print(msg['date'], "\t" + "\t" + "\t" + msg['message'])
    else:
        print("Dunno know how to parse this object:" + msg['id'])
