import json

def loadConfigFunctionsFile(filename):
    settings = {}

    with open(filename) as json_file:
        settings = json.load(json_file)

    return settings

def getFunctionObject(configObject,settingsTypeNameString, settingsSubTypeNameString):
    try:
        functObject = configObject.get(settingsTypeNameString).get(settingsSubTypeNameString)
        return functObject
    except:
        return ""
     