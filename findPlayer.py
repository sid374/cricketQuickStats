import urllib
import json
from bs4 import BeautifulSoup
from bs4 import element
import xml.etree.ElementTree as ET
from pymongo import MongoClient
from Tkinter import *
import ttk

client = MongoClient()
db = client.cricket
collection = db.statistics

Pname = "MS Dhoni"
def getPlayerInfo():
    result = collection.find_one({"player.fullName" : { '$regex': '.*'+playerName.get()+'.*', '$options': 'i' }})
    if result == None:
        resultName.set("Not found")
        resultNationality.set("Not Found")

    else:
        resultName.set(result['player']['fullName'])
        resultNationality.set(result['player']['nationality'])
        print(result['player']['fullName'])
        for matchType in result['stats']:
            if matchType['matchType'] == "IPLT20":
                for a,b in matchType['battingStats'].items():
                    formattedResult = str(a) + ": " + str(b)
                    print formattedResult
        print ("====================================")
        #stats = (result['stats']['nationality'])

def calculate(*args):
    try:
        value = float(playerName.get())
        resultName.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass


root = Tk()
root.title("Player Search")
mainframe = ttk.Frame(root,padding="3 3 12 12")
mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0,weight =1)

playerName = StringVar()
resultName = StringVar()
resultNationality = StringVar()
playerName_entry = ttk.Entry(mainframe, width=50, textvariable=playerName)
playerName_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=resultName).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=getPlayerInfo).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Name").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Player: ").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Nationality: ").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, textvariable=resultNationality).grid(column=4, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

playerName_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()







