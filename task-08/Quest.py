import json
import os
import requests
page=1
while True:
    json = requests.get('https://api.github.com/users/amfoss/repos?page='+str(page)).json()
    page+=1
    if len(json)==0:
        break
    for i in range(0,len(json)):
        os.system('perceval git --json-line '+json[i]['svn_url']+' >>commits.json')
