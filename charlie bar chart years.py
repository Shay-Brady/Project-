import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("parents.xlsx")
data=df["My son/daughter is in"]
count = {
  "1st Year": 0,
  "2nd Year": 0,
  "3rd Year": 0,
  "4th Year": 0,
  "5th Year": 0,
  "6th Year": 0,
}
for item in data:
    if item in count:
        count[item]+=1
    else:
        count[item]=1


x=list(count.keys())
h=list(count.values())
plt.bar(range(len(count)), h, tick_label=x)
plt.show()

    
        