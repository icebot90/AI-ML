import pandas as pd
import numpy as np

df=pd.read_csv('week-1/student_marks.csv')
all=df[["Maths","Physics","Chemistry","English","Biology","Economics","History","Civics"]].values
count=0
total=0
max=0
for i in all:
    total+=np.sum(i)
    if np.sum(i)>max:
        max=np.sum(i)
    np.nan_to_num(i)
    count+=1
print("Mean:",total/count)
print("Max:",max)