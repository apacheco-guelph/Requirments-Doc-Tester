# Configured to take a data list with [reqFile, catToTest]

def OnlyNumeric(dataType):
    reqFile = dataType[0]
    settingsObject = dataType[1]
    print("Ran only numeric")
    return {"400" : { "status" : "Success", "message" : "" , "code" : "400" } }