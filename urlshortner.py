#author: Subham Singh
#implementation of a Brand new URL Shortner Sevice its ready to deploy

import random

URLDict=dict()
alphabets="abcdefghijklmnopqrstuvwxyz"
numbers="0123456789"
alnum=list(alphabets+alphabets.upper()+numbers)


def createshortURL():
    shortURL=""
    while shortURL=="":
        while len(shortURL)<6:
            shortURL+=random.choice(alnum)
            if shortURL in URLDict.keys():
                shortURL=""
    return shortURL


def shortennonRedundand(newlongURL):
    for shortURL in URLDict.keys():
        if URLDict[shortURL]==newlongURL:
            return shortURL
    newshortURL=createshortURL()
    URLDict[newshortURL]=newlongURL
    return newshortURL


def shortenRedundand(newlongURL):
    newshortURL=createshortURL()
    URLDict[newshortURL]=newlongURL
    return newshortURL


def restore(shortURL):
    if shortURL in URLDict.keys():
        return URLDict[shortURL]
    else:
        return None
def main():
    URLs=["www.google.com","www.facebook.com","www.google.com",
    "www.amazon.com","www.spacex.com","www.xxx.com","www.tesla.com"]
    print("***** Non Redundant URL ******")
    for URL in URLs:
        shortURL=shortennonRedundand(URL)
        print("my.url/",shortURL,'-',restore(shortURL))


    print("****** Redundant URL *********")

    for URL in URLs:
        shortURL=shortenRedundand(URL)
        print("goo.gl/",shortURL,'-',restore(shortURL))
    print("******************************")
if __name__=="__main__":
    main()
