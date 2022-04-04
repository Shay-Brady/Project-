import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_excel("parents.xlsx")
data=df["Do you think your child learns better by using digital strategies like online quizzes, games, Power Point presentations, tutorial videos, clips etc. ?"]
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
plt.title("Do you think your child learns better by using digital strategies like online quizzes, games, Power Point presentations, tutorial videos, clips etc. ?")
plt.show()