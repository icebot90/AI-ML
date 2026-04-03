import pandas as pd
import numpy as np

df=pd.read_csv('week-1/student_marks.csv')
df.rename(columns={'Unnamed: 0': 'Name'},inplace=True)
all_marks=df[["Maths","Physics","Chemistry","English","Biology","Economics","History","Civics"]].values
print("Average of all students:",np.sum(all_marks)/len(all_marks))
subjects=["Maths","Physics","Chemistry","English","Biology","Economics","History","Civics"]
df['Total']=df[subjects].sum(axis=1)
print("Top Student is:",df.loc[df['Total']==df['Total'].max(),'Name'].values[0])
print(f"Average of Subjects are:\nMath: {np.mean(np.array(df['Maths']))}\nPhysics: {np.mean(np.array(df['Physics']))}\nChemistry: {np.mean(np.array(df['Chemistry']))}\nEnglish: {np.mean(np.array(df['English']))}\nBiology: {np.mean(np.array(df['Biology']))}\nEconomics: {np.mean(np.array(df['Economics']))}\nHistory: {np.mean(np.array(df['History']))}\nCivis: {np.mean(np.array(df['Civics']))}")
print(f"Topper of each Subjects are:\nMath: {df.loc[df['Maths']==df['Maths'].max(),'Name'].values[0]}\nPhysics: {df.loc[df['Physics']==df['Physics'].max(),'Name'].values[0]}\nChemistry: {df.loc[df['Chemistry']==df['Chemistry'].max(),'Name'].values[0]}\nEnglish: {df.loc[df['English']==df['English'].max(),'Name'].values[0]}\nBiology: {df.loc[df['Biology']==df['Biology'].max(),'Name'].values[0]}\nEconomics: {df.loc[df['Economics']==df['Economics'].max(),'Name'].values[0]}\nHistory: {df.loc[df['History']==df['History'].max(),'Name'].values[0]}\nCivics: {df.loc[df['Civics']==df['Civics'].max(),'Name'].values[0]}")
