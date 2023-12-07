import pandas as pd

sf = pd.DataFrame()

df1 =pd.read_excel('ameenpur_builder.xlsx')
df2 =pd.read_excel('bachupally_builder.xlsx')
df3 =pd.read_excel('kondapur_builder.xlsx')
df4 =pd.read_excel('miyapur_builder.xlsx')
df5 =pd.read_excel('shadnagar_builder.xlsx')

a1 = df1['links'].tolist()
a2 = df2['links'].tolist()
a3 = df3['links'].tolist()
a4 = df4['links'].tolist()
a5 = df5['links'].tolist()

c = set(a1+a2+a3+a4+a5)

sf['links'] =list(c)
sf.to_excel('Hyderabad_Builders_links_Database.xlsx',sheet_name='Sheet1',index=False)