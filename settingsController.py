from settingsFunctions import *
import json

errorCode = {
    "errorCode" : 200
}

def runSettingsFunction(nameOfSettingsFunction,dataTypeArray):
    # runs function 'nameOfSettingsFunction' gives RequirementsFile and RowToTest as parmaeters
    # ie) runSomeFunction(file,row)
    
    return getattr((globals()[nameOfSettingsFunction]),nameOfSettingsFunction)(dataTypeArray)

def getHeaderPosition(headersOrder,catToFind):
    settingsToCol = { 
        "ReqIDSettings" : "ReqID" , 
        "TimeEstimateSettings" : "Time",
        "PrioritySettings" : "Pri",
        "CatSettings" : "Cat",
        "UserSettings" : "User",
        "DependenciesSettings" : "Dep",
        "RequirementSettings" : "ReqDes"
    }
   
    for i in range(len(headersOrder)):
        if headersOrder[i] == settingsToCol.get(catToFind):
            return i

        


def configParams(nameOfSettingsFunction,reqFile,configObject,settingsObject,catToTest,headersOrder):
    configParamsList = []
    
    
    for params in configObject.get(catToTest).get("params"):
        if params == "reqFile":
            configParamsList.append(reqFile)
        if params == "configObject":
            configParamsList.append(configObject)
        if params == "settingsObject":
            configParamsList.append(settingsObject)
        if params == "catToTest":
            configParamsList.append(nameOfSettingsFunction)
        if params == "headersOrder":
            configParamsList.append(headersOrder)
        if params == "headerPosition":
            configParamsList.append(getHeaderPosition(headersOrder, nameOfSettingsFunction))
        
    
    return configParamsList


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
            #arrayToAdd.append(getConfigSettingsFunctionName(configFile,setting))
            arrayToAdd.append(setting)
        
        #iter(ObjectOfFunctionNames).next()[name] = arrayToAdd
        ObjectOfFunctionNames[name] = arrayToAdd

    return ObjectOfFunctionNames
