import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import Counter
df=pd.read_excel("parents.xlsx")
list1 = df["What activities from the list below help your child with their learning? You may select multiple answers"].tolist()
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
count["Orders From Teachers"] = count["Direct instruction from teacher"]
del count["Direct instruction from teacher"]
count["Notes/Answers"] = count["Sample notes/sample answers"]
del count["Sample notes/sample answers"]
count["Infographics"] = count["Mind Maps / Brainstorms / Graphic Organisers"]
del count["Mind Maps / Brainstorms / Graphic Organisers"]
count["Online Quizzes"] = count["Kahoot / Quizlet / Online Quizzes"]
del count["Kahoot / Quizlet / Online Quizzes"]
count["Personal Notes"] = count["Making their own notes"]
del count["Making their own notes"]
count["Groupwork"]= count["Pair group / groupwork "]
del count["Pair group / groupwork "]
count["PowerPoints"]=count["PowerPoint Presentations"]
del count["PowerPoint Presentations"]






#code to make the barchart and colour the bars
x=list(count.keys())
h=list(count.values())
plt.barh(range(len(count)), h, tick_label=x, color=(0.99, 0.4, 0.7777777, 0.5))
plt.show()