import json
settingsObject = {}
settings = {}


class objectify(object):
    def __init__(self, settings):
	    self.__dict__ = json.loads(settings)

def main():
    
    with open('settingsNew.json') as json_file:
        settings = json.load(json_file)

    settingsObject = objectify(json.dumps(settings))
    print(settingsObject.GeneralSettings)

main()