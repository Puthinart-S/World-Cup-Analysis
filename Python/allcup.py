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
"""Plot All Cups that each team got"""
matches = pd.read_csv("https://raw.githubusercontent.com/Puthinart-S/World-Cup-Analysis/master/wcfiles/Matches.csv")
cups = pd.read_csv("https://github.com/Puthinart-S/World-Cup-Analysis/raw/master/wcfiles/WorldCups.csv") #read the .csv file
cups["Winner"]=cups["Winner"].replace("Germany FR","Germany")
win = {}
dic =[]
for i in cups["Winner"]:
    if i in win:
        win[i] += 1
    else:
        win[i] = 1  #put the winner and amount of cups in dict
sortwin = sorted(win.items(), key=lambda kv: kv[1],reverse=True) #sort it
graphwin ={}
plt.figure(figsize=(10,4))
sea.set()
for i,j in sortwin:
    graphwin[i] = j

color= ["yellow","lawngreen","black","blue","lightblue","darkblue","white","red"]
sea.barplot(list(graphwin.keys()),list(graphwin.values()),palette=color)
plt.show()
