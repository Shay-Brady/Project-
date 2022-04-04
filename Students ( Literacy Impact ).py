#import packages
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_excel("Students.xlsx")
data=df.literacy_impact.to_list()
#list
count = {
    "No" : 0,
    "Yes" : 0
    }

for item in data:
    if item in count:
        count[item]+=1
    else:
        count[item]=1
        
#data for pie chart
labels = count.keys()
sizes = count.values()
explode = (0, 0)  
#plot pie chart
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=61)
ax1.axis('equal')
plt.title("Do you think that your literacy skills have been\n" + "impacted negatively by Covid?.", bbox={'facecolor':'0.8', 'pad':2})

plt.show()
