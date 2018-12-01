import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd
import requests
import seaborn as sea
from IPython import get_ipython
ipy = get_ipython()
if ipy is not None:
    ipy().run_line_magic('matplotlib', 'inline')
    ipy().run_line_magic('config', 'InlineBackend.figure_format = "retina"')  #import part


matches = pd.read_csv("https://raw.githubusercontent.com/Puthinart-S/World-Cup-Analysis/master/wcfiles/Matches.csv")
cups = pd.read_csv("https://github.com/Puthinart-S/World-Cup-Analysis/raw/master/wcfiles/WorldCups.csv") #read the .csv file


matches = matches.replace("IR Iran","Iran")
matches = matches.replace("Germany FR","Germany")
matches = matches.replace('rn">Republic of Ireland',"Ireland")
matches = matches.replace('rn">Bosnia and Herzegovina',"Bosnia and Herzegovina")
matches = matches.replace("C�te d'Ivoire","Ivory Coast") 
matches[['Home Team Name','Home Team Goals', 'Away Team Goals', 'Away Team Name']]
matches["Home Team Name"]=matches["Home Team Name"].replace("Germany FR","Germany")
matches["Home Team Name"]=matches["Home Team Name"].replace("Germany FR","Germany")#fix the wrong name
""" Plot number Win,Lose and Draw match of each team""" 
def win(matches):
    if matches["Home Team Goals"] > matches["Away Team Goals"]:
        return matches["Home Team Name"]
    if matches["Home Team Goals"] < matches["Away Team Goals"]:
        return matches["Away Team Name"]
    if matches["Home Team Goals"] == matches["Away Team Goals"]:
        return "DRAW"  #return the winner
def lost(matches):
    if matches["Home Team Goals"] < matches["Away Team Goals"]:
        return matches["Home Team Name"]
    if matches["Home Team Goals"] > matches["Away Team Goals"]:
        return matches["Away Team Name"]
    if matches["Home Team Goals"] == matches["Away Team Goals"]:
        return "DRAW"   #return the loser
 
matches["win-teams"]  = matches.apply(lambda matches:win(matches),axis=1) #put the return values inside match["win-teams"]
matches["lose-teams"] = matches.apply(lambda matches:lost(matches),axis=1)  #put the return values inside match["lose-teams"]
lost = matches["lose-teams"].value_counts().reset_index()  
win = matches["win-teams"].value_counts().reset_index() #Count how many win and lose
wl  = win.merge(lost) #put win and lose together in 1 chart
wl = wl[wl["index"] != "DRAW"]
wl.columns  = ["team","wins","loses"] 

matchplay={}
for i in wl["team"]:
     matchplay[i] = list(matches["Home Team Name"]).count(i)+list(matches["Away Team Name"]).count(i) # count all match that each team play
wl["match"]  =list(matchplay.values()) 
wl["draws"] = wl["match"]-(wl["wins"]+wl["loses"]) #draws game = matchplay-(lose+win)
wl = wl.sort_values(by="wins",ascending=True) #sort by win match
wl.index = wl.team #replace index by team name
wl[["wins","draws","loses"]].plot(kind="barh",stacked=True,figsize=(10,17),
                                 color=["green","blue","red"],
                                  linewidth=1, edgecolor="k"*len(wl))
plt.legend(loc="center right")
plt.xticks(np.arange(0,120,5))
plt.title("Match outcomes by countries")
plt.xlabel("matches played")
plt.show()
