import settingsLoader as config

def main():
    configObject = config.loadSettingsFile('settingsNew.json')
    
    #config.getGeneralSettings(configObject)
    #print(config.isTimeEstimateFloat(configObject))
    array = ["ReqID","Category","Usr","Requirement","Dependencies","Priority","TimeEstimate"]
    jsonToCatch = config.isHeadingCorrect(configObject,array)
    print(jsonToCatch)

main()