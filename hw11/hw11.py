import pandas as pd

df1 = pd.read_csv('hw10\provinces_updated.xls - Sheet1.csv')
# print(df1.head())

population_in_persons = df1['Population'] / df1['Area'] *1000
# print(df1.loc[df1['Name', population_in_persons]])


df2 = pd.read_excel('hw11\coastlines.xls')

df1['Coastline'] = df2['Coastline']
print(df1)

print(df2.head())