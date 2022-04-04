import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import Counter
df=pd.read_excel("parents.xlsx")
list1 = df["What are the main advantages to 58 minute classes for your child? You may select multiple answers."].tolist()
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
count["Less Stress"] = count["Less stress moving from place to place"]
del count["Less stress moving from place to place"]
count["Feels More Organised"] = count["It feels more organised"]
del count["It feels more organised"]
count["More Activities"] = count["Different types of activities can take place"]
del count["Different types of activities can take place"]
count["No Answer"] = count["nan"]
del count["nan"]
count["More Time For Tests"] = count["Better time available for assessments/tests"]
del count["Better time available for assessments/tests"]
count["More productive"] = count["More productive for getting topics covered"]
del count["More productive for getting topics covered"]
count["More Questioning"] = count["More time for questioning "]
del count["More time for questioning "]




#code to make the barchart and colour the bars
x=list(count.keys())
h=list(count.values())
plt.barh(range(len(count)), h, tick_label=x, color=(0.99, 0.4, 0.7777777, 0.5))
plt.show()








    
