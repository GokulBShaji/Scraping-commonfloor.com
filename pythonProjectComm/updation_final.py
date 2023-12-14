import pandas as pd
df1 = pd.read_excel('final.xlsx')
df2 = pd.read_excel('transpose_of_hyderabad_database_features.xlsx')
df3 = pd.read_excel('Distinct_Amenities.xlsx')

empty_lists = [[] for _ in range(140)]
empty = []
for i in range(1399):
    empty.append(i)

k = df3['Distinct Amenities'].to_list()

y = 0
x = 0
for m in empty:
    a = df2[m].to_list()
    for i in range(140):
        if k[i] in a:
            empty_lists[i].append('1')
            y+=1
            print(y)
        else:
            empty_lists[i].append('0')
            x+=1
            print(x)

print(empty_lists[86])
print(len(empty_lists[86]))
print(k[86])

for s in range(140):
    df1[f"{k[s]}"] = empty_lists[s]

df1.to_excel('final.xlsx',sheet_name='Sheet1',index=False)