def headersConnect(reqFile,catToTest,settingsObject):
    headersOrder = []
    for headers in reqFile[0]:
        for headersConnected in configObject.get("HeadersSettings").get("HeadersConnect"):
            if headers == configObject.get("HeadersSettings").get("HeadersConnect").get(headersConnected):
                headersOrder.append(str(headersConnected))
    return headersOrder