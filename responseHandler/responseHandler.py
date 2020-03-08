
import json

def readListOfAllResponses():
    responses = {}
    filename = 'responseHandler/listOfAllResponses.json'
    
    with open(filename) as json_file:
        responses = json.load(json_file)
    
    return responses

def getResponseFromCode(code):
    listOfAllResponses = readListOfAllResponses()
    print(listOfAllResponses.get(code))
    return listOfAllResponses.get(code)