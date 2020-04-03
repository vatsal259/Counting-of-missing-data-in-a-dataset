import pandas as pd
dataset=pd.read_csv('who_suicide_statistics.csv')
print("Number of missing data: ",end="")
print(dataset.isnull().sum().sum())
