import pandas as pd

df1 = pd.read_excel('hyderabad_builder_database_features.xlsx')
df2 = pd.read_excel('Distinct_Amenities.xlsx')


sf = pd.DataFrame()

Project_Name = df1['Project Name'].to_list()
Distinct = df2['Distinct Amenities'].to_list()

empty = []
for i in range(1399):
    empty.append(i)

sf['Project Name'] = Project_Name
for i in Distinct:
    sf[f"{i}"] = empty

sf.to_excel('final.xlsx',sheet_name='Sheet1',index=False)