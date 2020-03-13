import json, csv
import settingsController1 as settingsController
import configFunctionsLoader as listOfFunctions
from responseHandler import *

class requirementsFile:
    def __init__(self, filename, contentList):
        self.filename = filename
        self.contentList = contentList

class content:
    def __init__(self, ReqID, Cat, User, ReqDes, Dep, Pri, Time):
        self.ReqID = ReqID
        self.Cat = Cat
        self.User = User
        self.ReqDes = ReqDes
        self.Dep = Dep
        self.Pri = Pri
        self.Time = Time

def loadSettingsFile(filename):
    settings = {}

    with open(filename) as json_file:
        settings = json.load(json_file)
    
    return settings

def checkIfFileExists(stringForInput):
    toLoop = True
    filename = ""
    f = ""
    while(toLoop):
        try:
            print(stringForInput)
            filename = input(">")
            f = open(filename)
            toLoop = False
        except:
            print("File Does Not Exist")
        
    f.close()     
    return filename

def checkIfValidFile(stringForInput,typeOfFile,errorMessage):
    toLoop = True
    filename = ""
    while(toLoop):
        filename = checkIfFileExists(stringForInput)
        if filename.lower().endswith(typeOfFile):
            toLoop = False
        else:
            print(errorMessage)
    return filename

def getSettingFile():
    return checkIfValidFile("What is the name of the settings file you wish to use?",'.json',"Must be a valid settings file")

def getRequirementsFile():
    return checkIfValidFile("What is the name of the Requirements file you wish to use?",'.csv',"Must be a valid csv file")

def readCSV(filename):
    reqFile = ""
    with open(filename) as csv_file:
        csv_readerSaved = csv.reader(csv_file, delimiter=',')
        reqFile=[r for r in csv_readerSaved]
    
    return reqFile



def checkIt(configObject, functionsObject, reqFile, lineNumber):
    for topLayerSettings in configObject:
        print(topLayerSettings)
        for lowerLayerSettings in configObject.get(topLayerSettings):
            print("\t"+lowerLayerSettings)


def getRowNumberOfHeader(headersOrder, headerToFind):
    i = 0
    for header in headersOrder:
        if headerToFind == header:
            return i
        i = i + 1
    return -1

def getOrderOfHeaders(reqFile, configObject):
    #TODO - add error handling for if the headers are not all there and or there is some error
    headersOrder = []
    for headers in reqFile[0]:
        for headersConnected in configObject.get("HeadersSettings").get("HeadersConnect"):
            if headers == configObject.get("HeadersSettings").get("HeadersConnect").get(headersConnected):
                headersOrder.append(str(headersConnected))
    return headersOrder

def parseSettingsFile(configObject, functionsObject):
    arrayFromSettingsController = settingsController.parseSettingsFile(configObject,functionsObject)
    arrayFromResponseHandler = getattr((globals()["responseHandler"]),'cleanSettingsError')(arrayFromSettingsController)
    return arrayFromResponseHandler

def main():
    settingsFilename = getSettingFile()
    settingsObject = loadSettingsFile(settingsFilename)

    reqFilename = getRequirementsFile()
    reqFile = readCSV(reqFilename)

    configObject = loadSettingsFile('configFunctions.json')
    #checkIt(configObject,functionsObject,reqFile,0)

    headersOrder = getOrderOfHeaders(reqFile,settingsObject)
    #WORKS --> print(getRowNumberOfHeader(headersOrder,"Time"))
    
    #Working accepting of responses
    allResponsesObject = {}
    builtInFunctions = ['HeadersConnect']
    arrayFromSettingsController = settingsController.parseSettingsFile(settingsObject,configObject)
    for generalFunc in arrayFromSettingsController:
        arrayOfResponses = []
        print(generalFunc)
        for func in arrayFromSettingsController.get(generalFunc):
            if func not in builtInFunctions:
                funcParams = settingsController.configParams(generalFunc,reqFile,configObject,settingsObject,func,headersOrder)
                arrayOfResponses.append(settingsController.runSettingsFunction(configObject.get(func).get("functionName"),funcParams))


        allResponsesObject[generalFunc] = arrayOfResponses
    
    print()

    print("\n-------\nTesting\n-------")

    print("\n------------\nfunctionsObject\n------------")
    print(configObject)

    print("\n------------\nResponsesObject\n------------")
    print(allResponsesObject)
    
    





main()