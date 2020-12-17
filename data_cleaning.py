import pandas as pd 
df = pd.read_csv("glassdoor_jobs.csv")
df = df[df['Salary Estimate'] != '-1']
print(df.head(20))