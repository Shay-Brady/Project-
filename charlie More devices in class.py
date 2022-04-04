import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_excel("parents.xlsx")
data=df["Would you like your child to have more access to digital devices in lessons?"]
count={}
for item in data:
    if item in count:
        count[item]+=1
    else:
        count[item]=1


labels = count.keys() 
sizes = count.values()



fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  
plt.title("Would you like your child to have more access to digital devices in lessons?")
plt.show()