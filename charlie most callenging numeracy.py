import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_excel("parents.xlsx")
data=df["What aspects of numeracy does your child find most challenging?"]
count={
    "Algebra":0,
    #"Arithmetic":0,
    "Other":0,
    "Fractions/ Percentages":0,
    "Geometry":0,
    }
for item in data:
    if item in count:
        count[item]+=1
    else:
        count[item]=1
labels = count.keys() 
sizes = count.values()


fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow= False, startangle=90)
ax1.axis('equal')  
plt.title("What aspects of numeracy does your child find most challenging?")
plt.show()