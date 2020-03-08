from settingsFunctions import *
import json

class objectify(object):
    def __init__(self, settings):
	    self.__dict__ = json.loads(settings)

def loadSettingsFile(filename):
    settings = {}

    with open(filename) as json_file:
        settings = json.load(json_file)

    settingsObject = objectify(json.dumps(settings))
    
    return settings


def readSettingsFile(filename):
    settings = {}

    with open(filename) as json_file:
        settings = json.load(json_file)

    settingsObject = objectify(json.dumps(settings))
    
    return settings

def runSettingsFunction(nameOfSettingsFunction,RequirementsFile,RowToTest):
    getattr((globals()[nameOfSettingsFunction]),nameOfSettingsFunction)(RequirementsFile,RowToTest)

def getConfigSettings(configFile, settings):
    return configFile.get(settings).get("functionName")

def parseSettingsFile(settingsFile, configFile):
    arrayOfFunctionNames = []
    for setting in settingsFile.get('ReqIDSettings'):
        arrayOfFunctionNames.append(getConfigSettings(configFile,setting))

    return arrayOfFunctionNames
