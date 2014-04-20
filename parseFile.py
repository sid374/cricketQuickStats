import urllib
import json
from bs4 import BeautifulSoup
from bs4 import element
import xml.etree.ElementTree as ET
from pymongo import MongoClient


client = MongoClient()
db = client.cricket
collection = db.statistics

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


for i in range(2,2000):
    #changingurl = "http://www.iplt20.com/teams/royal-challengers-bangalore/squad/"+str(i)+"/chris-gayle"
    try:
        fo = open("./players/player"+str(i)+".txt", "r")
    except:
        continue
    toPost = fo.read()
    #print toPost
    jsonData = json.loads(toPost)
    insertId = collection.insert(jsonData)
    fo.close()
    print i






