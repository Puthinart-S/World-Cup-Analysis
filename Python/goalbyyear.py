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
"""Plot All Goals In Each Years"""
matches = pd.read_csv("https://raw.githubusercontent.com/Puthinart-S/World-Cup-Analysis/master/wcfiles/Matches.csv")
cups = pd.read_csv("https://github.com/Puthinart-S/World-Cup-Analysis/raw/master/wcfiles/WorldCups.csv") #read the .csv file

cups["Yearstr"] = cups["Year"].astype(str) #Change type to string
plt.figure(figsize=(13,7))
sea.set()
sea.barplot(cups["Yearstr"],cups["GoalsScored"])
plt.xlabel("Year")
plt.ylabel("Goals Scored")
plt.title("Goal Scored By Year")
plt.savefig("goalbyyear.svg")
plt.show() #show the graph

