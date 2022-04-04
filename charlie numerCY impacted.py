import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_excel("parents.xlsx")

data=df["Do you think that your child's numeracy skills have been negatively impacted by Covid?"]
count={}
for item in data:
    if item in count:
        count[item]+=1
    else:
        count[item]=1
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = count.keys()
sizes = count.values()
  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()