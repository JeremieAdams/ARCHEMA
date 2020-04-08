#jsonplay.py

import json

basePyDic = {'fields':[], 'order': []}
baseJSONObj = {'$schema': 'http://json-schema.org/draft-04/schema#','type': 'object', 'properties':[], 'propertiesOrder':[]}

#This function will control loading the json scheam into a pytoh dict object for conversion
def loadJson(data):
    data = json.loads(data)
    fillFields(data)
    fillOrder(data)
    #print(exportJson(basePyDic))
    return data

def fillFields(data):
    print(data)
    for each in data["properties"]:
        print(data["properties"][each]["type"])
    return

def fillOrder(data):
    for each in data["propertiesOrder"]:
        basePyDic["order"].append(each)
    return

def importJson(data):
    if jsonValidator(data):
        return loadJson(data)
    else:
        return "JSON Import failed. Please Validate Structure"

def jsonValidator(data):
    try:
        json.loads(data)
        return True
    except ValueError as error:
        print("Invalid Json: %s: " % error)
        return False


#The following functions will control loading the python dict into a json schema object for export
def exportJson(dic):
    return json.dumps(dic)

def dumpJson(data): 
    orderProperties(data)
    return json.dumps(baseJSONObj)

def orderProperties (data):
    for each in data['order']:
        baseJSONObj["propertiesOrder"].append(each)
    returngit i