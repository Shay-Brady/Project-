#import packages
import pandas as pd
import matplotlib.pyplot as plt
#read excel file
df=pd.read_excel("Students.xlsx")
data=df["I am in"]
#list
count={
    "1st Year" : 0,
    "2nd Year" : 0,
    "3rd Year" : 0,
    "Transition Year" : 0,
    "5th Year" : 0,
    "6th Year" : 0
    }
for item in data:
    if item in count:
        count[item]+=1
    else:
        count[item]=1
#plot bar chart
fig = plt.figure(figsize = (10, 5))
x=list(count.keys())
h=list(count.values())
plt.bar(range(len(count)), h, tick_label=x)
plt.show()
