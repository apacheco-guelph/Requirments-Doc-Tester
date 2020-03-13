# Configured to take a data list with [reqFile, catToTest, headerPosition]
import responseHandler
def OnlyNumeric(dataType):

    #Getting associated datatypes
    reqFile = dataType[0]
    catToTest = dataType[1]
    headerPos = dataType[2]
    
    #creating response array
    responseArray = []   

    i = 0
    for row in reqFile:
        if i != 0: #to skip the headers
            try:
                int(row[headerPos]) #checking to see if it is an int
                #if no error occured it assumes it is a valid int and appends a succes response to the response array
                responseArray.append(responseHandler.generateResponse('Success','is integer',catToTest,i,str(row[headerPos])))
            except:
                #Because of any possible exception it records a failure and appends to the response array accordingly
                responseArray.append(responseHandler.generateErrorResponse('Failure','is not integer',catToTest,i,"integer",str(row[headerPos])))
        i = i + 1
    
    return responseArray