import json

class objectify(object):
    def __init__(self, settings):
	    self.__dict__ = json.loads(settings)


jsonToThrow = {}

def getGeneralSettings(settingsObject):
    for item in settingsObject.GeneralSettings:
        print(item)
    
    print(settingsObject.GeneralSettings.get('EveryOtherLine'))
    print(settingsObject.HeadersSettings.get('HeadersConnect').get('Pri'))

def jsonToThrowSettingsError(possibleError):
    errorCode = -400
    while errorCode in jsonToThrow:
        errorCode = errorCode - 1

    jsonToThrow[errorCode] = {
        "Possible Settings Error" : possibleError
    }



def jsonToThrowExRec(status, expected, recieved):
    key = len(jsonToThrow)
    toSendDescr = "Expected: [" + expected + "], Recieved [" + recieved + "]"
    toSendTitle = ""
    
    if status:
        toSendTitle = "Success"
    else:
        toSendTitle = "Failure"
    
    jsonToThrow[key] = {
        toSendTitle : toSendDescr
    }


def isHeadingCorrect(settingsObject, array):
    
    headingVariables = settingsObject.HeadersSettings.get('HeadersConnect')
    headingUserFile = settingsObject.HeadersSettings.get('HeadersOrder')

    for headers in headingVariables:
        print(headers + ":" + headingVariables.get(headers))
        if headingVariables.get(headers) not in headingUserFile:
            print("wut")
            jsonToThrowSettingsError("Headers ordered and the connected headers do not matach")


    if settingsObject.HeadersSettings.get('HeadersOrdered'):

        for i in range(len(array)):
            if (headingUserFile[i] == array[i]):
                jsonToThrowExRec(True, headingUserFile[i], array[i])
            else:
                jsonToThrowExRec(False, headingUserFile[i], array[i])

    return jsonToThrow



def isTimeEstimateFloat(settingsObject):
    return settingsObject.TimeEstimateSettings.get('TimeEstimateFloat')

def loadSettingsFile(filename):
    settings = {}

    with open(filename) as json_file:
        settings = json.load(json_file)

    settingsObject = objectify(json.dumps(settings))
    
    return settingsObject

def main():
    print()
    

main()