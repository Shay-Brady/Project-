import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
df=pd.read_excel("Students.xlsx")
list1 = df["Are there any disadvantages to 58 minute classes for your learning? You may select multiple answers"].tolist()

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


x=list(count.keys())
h=list(count.values())
plt.barh(range(len(count)), h, tick_label=x)
plt.show()