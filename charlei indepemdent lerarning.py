import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import Counter
df=pd.read_excel("parents.xlsx")
list1 = df["Independent learning and critical thinking skills are essential for my child's learning experience."].tolist()
#splits up the code so it can be order in the dictionary
b=[]
for element in list1:
    element = str(element)
    b.append(element.split(";"))
print(b)
a = pd.Series( (v[0] for v in b) )
#puts the data from the new list into a dictionary
count={}
for item in a:
    if item in count:
        count[item]+=1
    else:
        count[item]=1
print(count)
#makes new keys for the dictionary
"""count["Teachers Talk A lot"] = count["Too much teacher talk "]
del count["Too much teacher talk "]
count["Less Time w/ Teacher"] = count["Less contact time with subject teachers throughout the week"]
del count["Less contact time with subject teachers throughout the week"]
count["Lack Of Focus"] = count["It is difficult to stay concerned on one subject for a long period of time"]
del count["It is difficult to stay concerned on one subject for a long period of time"]
count["No Answer"] = count["nan"]
del count["nan"]
count["Forgetting Materials"] = count["Resources (not having all books for classes each day) "]
del count["Resources (not having all books for classes each day) "]"""





#code to make the barchart and colour the bars
x=list(count.keys())
h=list(count.values())
plt.barh(range(len(count)), h, tick_label=x, color=(0.99, 0.4, 0.7777777, 0.5))
plt.show()