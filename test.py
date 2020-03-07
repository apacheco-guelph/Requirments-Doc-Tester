#from settingsFunctions import *
from settingsFunctions import *
from responseHandler import *

import settingsController1
import importlib
import os

def main():
    files = [f for f in os.listdir('./settingsFunctions') if f != '__pycache__']
    #rH.hi()
    # Works --> getattr((globals()["helloTwo"]),'hip')()
    #getattr((globals()["hello"]),'hello')()
    a = settingsController1.readSettingsFile('settingsNew.json')
    b = settingsController1.readSettingsFile('configFunctions.json')
    #settingsController1.parseSettingsFile(a,b)

    #Response Handler error call --> getattr((globals()["responseHandler"]),'getResponseFromCode')('400')


main()