#import packages
import matplotlib.pyplot as plt
import pandas as pd
#read excel file
df=pd.read_excel("Students.xlsx")
data=df.independent_learning.to_list()
print(data)
#list
count = {
    "Disagree" : 0,
    "Strongly agree" : 0,
    "Strongly disagree" : 0,
    "Neutral" : 0,
    "Agree" : 0,
    }

for item in data:
    if item in count:
        count[item]+=1
    else:
        count[item]=1
        
#pie chart data
labels = count.keys()
sizes = count.values()
explode = (0, 0, 0, 0, 0, 0)  
#pie chart
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

plt.show()
        



            
