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

""" Plot top 20 team with the most goal in FIFA World Cup History"""
goal={}
for home,score in zip(matches["Home Team Name"],matches["Home Team Goals"]):
    if home in goal:
        goal[home] += score
    else:
        goal[home] = score #Count home team goals
for away,score in zip(matches["Away Team Name"],matches["Away Team Goals"]):
    if away in goal:
        goal[away] += score
    else:
        goal[away] = score #Count away team goals
sortedgoal = sorted(goal.items(), key=lambda i:i[1])
sortedgoal.reverse() #sort from max to min
teamname = []
goal = []
for i,j in sortedgoal:
    teamname.append(i)
    goal.append(j) #append team name and goals in list for plotting
plt.figure(figsize=(13,7))
sea.set()
graph = sea.barplot(teamname[:20],goal[:20])

graph.set_xticklabels(graph.get_xticklabels(),rotation=45)
plt.xlabel("Team")
plt.ylabel("Goals Scored")
plt.title("Top 20 Team Goals In FIFA World Cup")
plt.show()
