# Configured to take a data list with [reqFile, settingsObject, catToTest, headerPosition]
import responseHandler
def categoryStrictSort(dataType):

    #Getting associated datatypes
    reqFile = dataType[0]
    settingsObject = dataType[1]
    catToTest = dataType[2]
    headerPos = dataType[3]
    
    #creating response array
    responseArray = []   
    
    caseSensitive = False
    #checking if case sensitive
    try:
        caseSensitive = settingsObject.get('CatSettings').get('caseSensitive')
    except:
        caseSensitive = False


    i = 0
    catArrayPos = 0
    for row in reqFile:
        if i != 0: #to skip the headers
            try:
                array = settingsObject.get('CatSettings').get('categoryStrictSort')
                itemToCheck = row[headerPos]
                if not caseSensitive:
                    itemToCheck = itemToCheck.lower()
                    for j in range(len(array)):
                        array[j] = array[j].lower()

                if itemToCheck not in array:
                    responseArray.append(responseHandler.generateErrorResponse('Failure','category doesnt exist in settings file',catToTest,i,"",str(itemToCheck)))
                if itemToCheck in array:
                    if array.index(itemToCheck) < catArrayPos:
                        responseArray.append(responseHandler.generateErrorResponse('Failure','categories not sorted correctly',catToTest,i,"",str(itemToCheck)))
                    else:
                        catArrayPos = array.index(itemToCheck)
                        responseArray.append(responseHandler.generateResponse('Success','is sorted correctly',catToTest,i,str(itemToCheck)))
            except:
                #Because of any possible exception it records a failure and appends to the response array accordingly
                responseArray.append(responseHandler.generateErrorResponse('Failure','an Error was found',catToTest,i,"",str(itemToCheck)))
        i = i + 1
    
    return responseArray