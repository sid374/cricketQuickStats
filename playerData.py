import urllib
import json
from bs4 import BeautifulSoup
from bs4 import element
import xml.etree.ElementTree as ET
from pymongo import MongoClient


client = MongoClient()
db = client.cricket

firstName = ""
lastName = ""

def getPlayerName(playerSoup):
    matches = playerSoup.select(".playerBio h1")
    firstName = list(matches[0].descendants)[0].string.strip()
    lastName = list(matches[0].descendants)[1].string.strip()
    print("Player: "+firstName+" "+lastName)

def getPlayerstats(playerSoup):
    matches = playerSoup.select(".unitContent > div")
    print matches
    # for child in matches[0].descendants:
    #     print child


for i in range(1000,10000):
    #changingurl = "http://www.iplt20.com/teams/royal-challengers-bangalore/squad/"+str(i)+"/chris-gayle"
    flag =0
    changingurl = "http://dynamic.pulselive.com/dynamic/data/core/cricket/careerStats/"+str(i)+"_careerStats.js?_1397772296778="
    try:
        sock = urllib.urlopen(changingurl)
    except Exception:
        pass

    htmlSource = sock.read()
    htmlSource = htmlSource[20:len(htmlSource)-2]
    try:
        decoded = json.loads(htmlSource)
    except:
        flag = 1

    if flag == 0:
        fo = open("./players/player"+str(i)+".txt", "wb")
        fo.write(htmlSource);
        fo.close()
        print decoded['player']['fullName']
    # for i in decoded['stats']:
    #     if i['matchType'] == "IPLT20":
    #         print i['battingStats']


    sock.close()

    soup = BeautifulSoup(htmlSource)

    if "Error 404 - Page not found." in (soup.get_text()):
        pass

    else:
        #getPlayerName(soup)
        #getPlayerstats(soup)
        pass




