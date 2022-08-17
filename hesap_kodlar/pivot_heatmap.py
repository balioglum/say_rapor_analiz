import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

df=pd.read_csv('/home/ubuntu/say_rapor_analiz/hesap_kodlar/SON_joinli.csv',header=0)

data= pd.pivot_table(df, values='FREKANS', index='HESAP_ADI', columns='KURUM', aggfunc=np.sum)

print(data)
# f, ax = plt.subplots(figsize=(15, 6))
# sns.heatmap(data, annot=True, fmt="d", linewidths=.5, ax=ax)