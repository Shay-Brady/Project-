import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_excel("Students.xlsx")
data=df.digital_strategies.to_list()

count = {
    "No" : 0,
    "Yes" : 0
    }

for item in data:
    if item in count:
        count[item]+=1
    else:
        count[item]=1
        

labels = count.keys()
sizes = count.values()
explode = (0.1, 0, 0)  

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=60)
ax1.axis('equal')
plt.title("Do you think you learn better by using digital strategies?", bbox={'facecolor':'0.8', 'pad':2})

plt.show()