import pandas as pd
df=pd.read_csv('/home/ubuntu/say_rapor_analiz/hesap_kodlar/hesap_plan_tum.csv', delimiter=";", header=0)
df_sonuc=pd.read_csv('/home/ubuntu/say_rapor_analiz/hesap_kodlar/sonuç.csv',header=0)
# print(df)

# print(df['HESAP_ADI'])

cols = df.select_dtypes(object).columns
df[cols] = df[cols].apply(lambda x: x.str.strip())

df['HESAP']=df['HESAP_KOD'].astype(str)+" "+df['HESAP_ADI'].str.split(' ').str[0]


#df[['Street', 'City', 'State']] = df['Address'].str.split(',', expand=True)

print(df)
df.to_csv('/home/ubuntu/say_rapor_analiz/hesap_kodlar/sonuçla_join_yapılacak_hesap_adları.csv', index=False)

df_joinli=pd.merge(df, df_sonuc, on='HESAP',  how='inner')
df_joinli.to_csv('/home/ubuntu/say_rapor_analiz/hesap_kodlar/joinli.csv',index=False)

