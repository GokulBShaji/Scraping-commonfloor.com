import pandas as pd

df = pd.read_excel('hyderabad_builder_database_features.xlsx')
df = df.transpose()

df.to_excel('transpose_of_hyderabad_database_features.xlsx',sheet_name='Sheet1',index=False)