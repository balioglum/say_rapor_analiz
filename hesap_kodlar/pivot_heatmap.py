from operator import index
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df=pd.read_csv('/home/ubuntu/say_rapor_analiz/hesap_kodlar/SON_joinli.csv',header=0)

print(df.dtypes)
df['HESAP_ADI']=df['HESAP_KOD'].astype(str)+" "+df['HESAP_ADI'].astype(str)

data= pd.pivot_table(df, values='FREKANS', index='HESAP_ADI', columns='YIL', aggfunc=np.sum,fill_value=0)


print(data)

print(data.dtypes)


data.to_csv('/home/ubuntu/say_rapor_analiz/hesap_kodlar/hesap_kodu_yil_pivot.csv', encoding="utf-8-sig", sep="|")

#plot
fig, ax = plt.subplots(figsize=(16,48))
swarm_plot=sns.heatmap(data,fmt='.3g',cmap="YlGnBu", annot=True,cbar=False)
fig = swarm_plot.get_figure()
fig.savefig("/home/ubuntu/say_rapor_analiz/hesap_kodlar/pivot_heatmap.png") 