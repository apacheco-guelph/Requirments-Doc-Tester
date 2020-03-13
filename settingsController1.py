from settingsFunctions import *
import json

errorCode = {
    "errorCode" : 200
}

def runSettingsFunction(nameOfSettingsFunction,RequirementsFile,RowToTest):
    # runs function 'nameOfSettingsFunction' gives RequirementsFile and RowToTest as parmaeters
    # ie) runSomeFunction(file,row)
    getattr((globals()[nameOfSettingsFunction]),nameOfSettingsFunction)(RequirementsFile,RowToTest)

def getConfigSettingsFunctionName(configFile, settings):    
    try:
        return configFile.get(settings).get("functionName")
    except:
        return errorCode
    

def parseSettingsFile(settingsFile, configFile):
    ObjectOfFunctionNames = {}
    for name in settingsFile:
        arrayToAdd = []
        for setting in settingsFile.get(name):
            arrayToAdd.append(getConfigSettingsFunctionName(configFile,setting))

        
        #iter(ObjectOfFunctionNames).next()[name] = arrayToAdd
        ObjectOfFunctionNames[name] = arrayToAdd

    return ObjectOfFunctionNames
