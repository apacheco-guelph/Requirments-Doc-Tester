# Configured to take a data list with [reqFile, catToTest]
from responseHandler import responseHandler 
def OnlyNumeric(dataType):
    print(dataType)
    reqFile = dataType[0]
    settingsObject = dataType[1]
    catToTest = dataType[2]
    headersOrder = dataType[3]
    returned = responseHandler.generateResponse('Success','Line is Numeric',catToTest,'1')
    print("Ran only numeric")
    i = 0
    for header in headersOrder:
        if catToTest == header:
            break
        i = i + 1

    
    for row in reqFile:
        print(row[0])
            
    return returned