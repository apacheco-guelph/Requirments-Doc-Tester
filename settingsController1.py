from settingsFunctions import *
import json

class objectify(object):
    def __init__(self, settings):
	    self.__dict__ = json.loads(settings)

#def runFunctionSettings(requirementsFile, functions):


def readSettingsFile(filename):
    settings = {}

    with open(filename) as json_file:
        settings = json.load(json_file)

    settingsObject = objectify(json.dumps(settings))
    
    return settings

#def getConfigSettings(settings, configFile):
    

def parseSettingsFile(settingsFile, configFile):
    for setting in settingsFile.get('ReqIDSettings'):
        getConfigSettings(setting,configFile)

    print(settingsFile.get('ReqIDSettings'))
