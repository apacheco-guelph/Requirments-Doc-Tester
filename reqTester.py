import json, csv
import settingsController1 as config
import configFunctionsLoader as listOfFunctions

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

def main():
    configFilename = getSettingFile()
    configObject = config.loadSettingsFile(configFilename)

    reqFilename = getRequirementsFile()
    reqFile = readCSV(reqFilename)

    functionsObject = config.loadSettingsFile('configFunctions.json')
    #checkIt(configObject,functionsObject,reqFile,0)

    headersOrder = getOrderOfHeaders(reqFile,configObject)
    print(getRowNumberOfHeader(headersOrder,"Time"))
    
    for i in headersOrder:
        print(i + ",")

    #print(config.getConfigSettings(functionsObject,"OnlyNumeric"))
    arrayOfFunctionNames = config.parseSettingsFile(configObject,functionsObject)

    for func in arrayOfFunctionNames:
        config.runSettingsFunction(func,reqFile,"ReqID")





main()