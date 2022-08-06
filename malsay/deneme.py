from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd

def fuzzy_merge(df_1, df_2, key1, key2, threshold=90, limit=2):
    """
    :param df_1: the left table to join
    :param df_2: the right table to join
    :param key1: key column of the left table
    :param key2: key column of the right table
    :param threshold: how close the matches should be to return a match, based on Levenshtein distance
    :param limit: the amount of matches that will get returned, these are sorted high to low
    :return: dataframe with boths keys and matches
    """
    s = df_2[key2].tolist()
    
    m = df_1[key1].apply(lambda x: process.extract(x, s, limit=limit))    
    df_1['matches'] = m
    
    m2 = df_1['matches'].apply(lambda x: ', '.join([i[0] for i in x if i[1] >= threshold]))
    df_1['matches'] = m2
    
    return df_1

cols=["KURUM","YIL","BASLIK"]
df=pd.read_csv('/root/kurum_bulgu.csv',usecols = cols)



print(df.info())

cols = df.select_dtypes(object).columns
df[cols] = df[cols].apply(lambda x: x.str.strip())
df[['BULGU_NO', 'BULGU_ADI']] = df['BASLIK'].str.split(':', expand=True)

print(df)

x=fuzzy_merge(df, df, 'BASLIK', 'BASLIK', threshold=95, limit=2)

x.to_csv("matching.csv",header=True,index=False)


