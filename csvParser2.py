import csv
import json
import sys
from colorama import Fore, Back, Style, init
from grammarbot import GrammarBotClient
import math
import curses


settings = {}
settingsObject = {}
allRows = ""
keyOfErrors = 0

class objectify(object):
    def __init__(self, settings):
	    self.__dict__ = json.loads(settings)

class my_dictionary(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value

class ErrorObject:
    def __init__(self, reqId, errorName):
        self.reqId = reqId
        self.errorName = errorName

def readSettings():
    global settings
    with open('settings.json') as json_file:
        settings = json.load(json_file)

def readCSV(filename):
    global allRows
    with open(filename, encoding="utf-8") as csv_file:
        csv_readerSaved = csv.reader(csv_file, delimiter=',')
        allRows=[r for r in csv_readerSaved]

def generateErrorObject(reqId, error):  
    return ErrorObject(reqId,error)

def addToReport(listOfErrors, error):
    global keyOfErrors
    listOfErrors.add(keyOfErrors,error)
    keyOfErrors += 1

def organizeList(listOfErrors):
    organizeList = my_dictionary()
    sizeOfDictionary = len(listOfErrors)
    for i in range(sizeOfDictionary):
        
        if i > 0 and i < len(allRows):
            
            reqList = my_dictionary()
            iterate = 0
            for j in range(sizeOfDictionary):
                
                if listOfErrors[j].reqId == str(i):
                    iterate += 1
                    reqList.add(iterate,listOfErrors[j].errorName)
  
            organizeList.add(i,reqList)
    return organizeList

def printErrorReport(listOfErrors):
    numOfErrors = len(listOfErrors)
    for idList in listOfErrors:
        print("Requirement ID: " + str(idList) + "\n")
        
        for error in listOfErrors[idList]:
            errorFound = listOfErrors[idList]
            print("\t" + errorFound[error] + "\n")

    
    

def checkHeaders(listOfErrors):
    count = 0
    for header in settings.get("Headers"):
        if(header != allRows[0][count]):
            #print("NOPE{"+header+"}"+allRows[0][count]+"}\n") #add error handling
            addToReport(listOfErrors,generateErrorObject(0,"Incorrect Header Found: expected ["+header+"] but got ["+allRows[0][count]+"]"))
        
        count += 1

def searchDependencies(toSearch, toFind):
    category = (settingsObject.Category)
    toSearch = str(toSearch).strip('\'[]')
    for depend in category.get(toSearch).get('Dependencies'):
        if(depend == toFind):
            return toFind

    if len(category.get(toSearch).get('Dependencies')) <= 0:
        return

    return ""

def sortedCorrectly(listOfErrors):
    previousCategory = allRows[1][1]
    i = 0
    for Rows in allRows:
        if(allRows[i][0] != str(i) and i != 0):
            addToReport(listOfErrors,generateErrorObject(str(i),"ReqID not in correct order, got ["+allRows[i][0]+"], expected ["+str(i)+"]"))
        if(allRows[i][1] != previousCategory) and i != 0:
            toSearch = searchDependencies([allRows[i][1]],previousCategory)
            if(toSearch == ""):
                #print(str(i) + ">ERROR>"+ searchDependencies([allRows[i][1]],allRows[i][1]))
                addToReport(listOfErrors,generateErrorObject(str(i),"Category is not sorted correctly, got ["+searchDependencies([allRows[i][1]],allRows[i][1])+"] after a ["+previousCategory+"]"))
        if i != 0:
            previousCategory = allRows[i][1]
        i += 1

def searchPriorities(toSearch, toFind):
    category = (settingsObject.Category)
    toSearch = str(toSearch).strip('\'[]')
    toFind = str(toFind).strip('\'[]')
    for depend in category.get(toSearch).get('Priority'):
        if str(depend) == toFind:
            return toFind

    if len(category.get(toSearch).get('Priority')) <= 0:
        return

    return ""

def searchDependencies(toSearch, toFind):
    category = (settingsObject.Category)
    toSearch = str(toSearch).strip('\'[]')
    for depend in category.get(toSearch).get('Dependencies'):
        if(depend == toFind):
            return toFind

    if len(category.get(toSearch).get('Dependencies')) <= 0:
        return

    return ""

def checkGrammar(listOfErrors,client):
    i = 0
    if (client) != "":
        
        for Rows in allRows:
            stringToCheck = allRows[i][3]
            res = client.check(stringToCheck)
            if(len(res.matches) != 0):
                addToReport(listOfErrors,generateErrorObject(str(i),res.matches[0].message))
            i += 1

def checkPriority(listOfErrors):
    i = 0
    for Rows in allRows:
        if(allRows[i][1]) and i != 0:
            toSearch = searchPriorities([allRows[i][1]],[allRows[i][5]])
            if(toSearch == ""):
                #print(str(i) + ">ERROR PRI>"+ searchDependencies([allRows[i][1]],allRows[i][5]))
                addToReport(listOfErrors,generateErrorObject(str(i),"Priority Error, category ["+str(allRows[i][1])+"] had priority [" + str(allRows[i][5])+"]"))

        i += 1

def checkDepenedencies(listOfErrors):
    i = 0
    for Rows in allRows:
        if(allRows[i][1]) and i != 0:
            dependent = allRows[i][4]
            dependent = str(dependent).strip('\'[]')
            if(dependent != ""):
                dependent = int(allRows[i][4])
                if(dependent >= len(allRows)):
                    addToReport(listOfErrors,generateErrorObject(str(i),"Dependency out of range"))
                else:
                    toSearch = searchDependencies([allRows[i][1]],[allRows[dependent][4]])
                    if(i > dependent):
                        addToReport(listOfErrors,generateErrorObject(str(i),"Dependency cannot be referenced after the requirement: requirement "+ str(i) + " is after requirement " + str(dependent)))

                    if(toSearch == ""):
                        addToReport(listOfErrors,generateErrorObject(str(i),"Invalid dependency, ["+str(allRows[i][1])+"] cannot be dependent on [" + str(allRows[dependent][1]) + "]"))

        i += 1

def searchTimeEstimate(toSearch):
    category = (settingsObject.Category)
    toSearch = str(toSearch).strip('\'[]')
    return category.get(toSearch).get('TimeEstimate')

def timeEstimateCheck(listOfErrors):
    i = 0
    for Rows in allRows:
        if(allRows[i][1]) and i != 0:
            te = allRows[i][6]
            te = str(te).strip('\'[]')
            booleanIn = bool(searchTimeEstimate(allRows[i][1]))
            if(te != ""):
                if(len(te) > 0 and not booleanIn):
                    addToReport(listOfErrors,generateErrorObject(str(i),"Invalid time esitmate, [" + allRows[i][1]+ "] cannot have a time estimate, got ["+str(te)+"]"))

            if(te == "" and booleanIn):
                addToReport(listOfErrors,generateErrorObject(str(i),"Invalid time estimate, got ["+allRows[i][6]+"]"))
        i += 1


def main():
    global settingsObject
    readSettings()
    settingsObject = objectify(json.dumps(settings))
    client = ""
    if(hasattr(settingsObject,'GrammarBotClient')):
        client = GrammarBotClient(api_key=settingsObject.GrammarBotClient)
    
    print("\nWhat is the files name you wish to test")
    filename = input(">")
    readCSV(filename)
    listOfErrors = my_dictionary()
    checkHeaders(listOfErrors)
    sortedCorrectly(listOfErrors)
    checkPriority(listOfErrors)
    checkDepenedencies(listOfErrors)
    timeEstimateCheck(listOfErrors)
    checkGrammar(listOfErrors,client)
    counter = 0
    
    printErrorReport(organizeList(listOfErrors))
    #print(allRows)

main()