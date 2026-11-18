import pandas as pd
print("hello world")


import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import seaborn as sns
df = sns.load_dataset("tips")
print(df.head())


print(df.tail())
print(df.describe())
print(df.info())
print(df.dtypes)
print(df.columns)

df[['total_bill', 'tip', 'day', 'time']].head()

df.iloc[0]
print(df.iloc[0])

df.iloc[10:20]


df.loc[0:5, ['total_bill', 'tip']]

df[df['day'] == 'Sun']


df[(df['day'] == 'Sun') & (df['total_bill'] > 20)]

df.query("day == 'Sun' and total_bill > 20")

df[df['total_bill'] > 25]

print(df[df['total_bill'] > 25])
count = df[df['total_bill'] > 25].count()
print(count)



count = df.duplicated().sum()
print(count)



df.groupby('day')['tip'].mean()
df.groupby('sex')[['total_bill', 'tip']].mean()


df[['total_bill', 'tip', 'day', 'time']].head()
df.iloc[0]
df.iloc[10:20]
df.loc[0:5, ['total_bill', 'tip']]





















