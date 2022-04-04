import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_excel("parents.xlsx")
data=df["Does your child find Microsoft Teams and One Note beneficial for learning and their homework?"]
count={}
for item in data:
    if item in count:
        count[item]+=1
    else:
        count[item]=1
labels = count.keys() 
sizes = count.values()
explode = (0, 0)  

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  
plt.title("Does your child find Microsoft Teams and One Note beneficial for learning and their homework?")
plt.show()