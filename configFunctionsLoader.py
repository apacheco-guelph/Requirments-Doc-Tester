import json

errorCode = {
    "errorCode" : 200
}

def getFunctionObject(configObject,settingsTypeNameString, settingsSubTypeNameString):
    try:
        functObject = configObject.get(settingsTypeNameString).get(settingsSubTypeNameString)
        return functObject
    except:
        return errorCode
     