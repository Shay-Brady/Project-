#import packages
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
df=pd.read_excel("Students.xlsx")
list1 = df["most_challenging"].tolist()
#split data
b=[]
for element in list1:
    element = str(element)
    b.append(element.split(";"))
print(b)

a = pd.Series( (v[0] for v in b) )
#list
count={}
for item in a:
    if item in count:
        count[item]+=1
    else:
        count[item]=1

#data and plotting pie chart
x=list(count.keys())
h=list(count.values())
plt.barh(range(len(count)), h, tick_label=x)
plt.show()
