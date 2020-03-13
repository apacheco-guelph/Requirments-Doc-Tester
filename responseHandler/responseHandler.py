import json

generalResponse = {
    "status" : "",
    "message" : "" ,
    "from" : "",
    "lineNumber" : ""
}

def cleanSettingsError(arrayOfSettings):
    generalToUpdate = {}
    
    for settings in arrayOfSettings:
        arrayToUpdate = []
        
        for toClean in arrayOfSettings.get(settings):
            try:
                objectToAdd = {}
                objectToAdd['response'] = getResponseFromCode(toClean.get('errorCode'))
                toString = str(objectToAdd)
                arrayToUpdate.append(toString)          
            except:
                arrayToUpdate.append(str(toClean))
                pass

        stringATU = str(arrayToUpdate).replace("\"","")
        
        generalToUpdate[settings] = stringATU
    
    return generalToUpdate

def readListOfAllResponses():
    responses = {}
    filename = 'responseHandler/listOfAllResponses.json'
    
    with open(filename) as json_file:
        responses = json.load(json_file)
    
    return responses

def getResponseFromCode(code):
    listOfAllResponses = readListOfAllResponses()
    return listOfAllResponses.get(str(code))

def generateResponse(status,message,fromFunction,lineNumber):
    general = {}
    general['status'] = status
    general['message'] = message
    general['from'] = fromFunction
    general['lineNumber'] = lineNumber
    return general