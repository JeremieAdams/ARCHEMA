#main.py

import json
import utils
import jsonToFrom

with open('testfiles/example.json', 'r') as f:
    data = f.read()

dic = jsonToFrom.importJson(data)
#print(dic)
#print(jsonToFrom.exportJson(dic))