import pandas as pd

sf = pd.read_excel('hyderabad_builder_database_features.xlsx')
df = pd.DataFrame()

a1 = sf['Project Name'].to_list()
a2 = sf['feature_1'].to_list()
a3 = sf['feature_2'].to_list()
a4 = sf['feature_3'].to_list()
a5 = sf['feature_4'].to_list()
a6 = sf['feature_5'].to_list()
a7 = sf['feature_6'].to_list()
a8 = sf['feature_7'].to_list()
a9 = sf['feature_8'].to_list()
a10 = sf['feature_9'].to_list()
a11 = sf['feature_10'].to_list()
a12 = sf['feature_11'].to_list()
a13 = sf['feature_12'].to_list()
a14 = sf['feature_13'].to_list()
a15 = sf['feature_14'].to_list()
a16 = sf['feature_15'].to_list()
a17 = sf['feature_16'].to_list()
a18 = sf['feature_17'].to_list()
a19 = sf['feature_18'].to_list()
a20 = sf['feature_19'].to_list()
a21 = sf['feature_20'].to_list()
a22 = sf['feature_21'].to_list()
a23 = sf['feature_22'].to_list()
a24 = sf['feature_23'].to_list()
a25 = sf['feature_24'].to_list()
a26 = sf['feature_25'].to_list()
a27 = sf['feature_26'].to_list()
a28 = sf['feature_27'].to_list()
a29 = sf['feature_28'].to_list()
a30 = sf['feature_29'].to_list()
a31 = sf['feature_30'].to_list()
a32 = sf['feature_31'].to_list()
a33 = sf['feature_32'].to_list()
a34 = sf['feature_33'].to_list()
a35 = sf['feature_34'].to_list()
a36 = sf['feature_35'].to_list()
a37 = sf['feature_36'].to_list()
a38 = sf['feature_37'].to_list()
a39 = sf['feature_38'].to_list()
a40 = sf['feature_39'].to_list()

b = a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 + a11 + a12 + a13 + a14 + a15 + a16 + a17 + a18 + a19 + a20 + a31 + a32 + a33 + a34 + a35 + a36 + a37 + a38 + a39 + a40 + a21 + a22 + a23 + a24 + a25 + a26 + a27 + a28 + a29 + a30
c = set(b)
d = list(c)
print(d)
print(len(d))

df['Distinct Amenities'] = d
df.to_excel('Distinct_Amenities.xlsx',sheet_name='Sheet1',index=False)


