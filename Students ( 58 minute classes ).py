import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
df=pd.read_excel("Students.xlsx")
list1 = df["What are the main advantages to 58 minute classes for you? You may select multiple answers."].tolist()

b=[]
for element in list1:
    element = str(element)
    b.append(element.split(";"))
print(b)

a = pd.Series( (v[0] for v in b) )

count={}
for item in a:
    if item in count:
        count[item]+=1
    else:
        count[item]=1

labels = count.keys()
sizes = count.values()
explode = (0, 0, 0, 0, 0, 0, 0, 0)  

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=61)
ax1.axis('equal')

plt.show()