import settingsLoader as settings
import configFunctionsLoader as config

def OnlyNumeric(string):
    
    if string == "hello":
        print("Shamlom")
    else:
        print("goodbye")

def main():
    settingsObject = settings.loadSettingsFile('settingsNew.json')
    
    #settings.getGeneralSettings(settingsObject)
    #print(settings.isTimeEstimateFloat(settingsObject))
    array = ["ReqID","Category","Usr","Requirement","Dependencies","Priority","TimeEstimate"]
    jsonToCatch = settings.isHeadingCorrect(settingsObject,array)
    #print(jsonToCatch)

    configObject = config.loadConfigFunctionsFile('configFunctions.json')
    print(config.getFunctionObject(configObject,"ReqID","OnlyNumeric"))

    #globals()[config.getFunctionObjectName(reqFunctionObject)]("hello")

main()