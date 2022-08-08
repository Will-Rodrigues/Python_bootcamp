# -*- coding: utf-8 -*-
"""lesson_72.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u_TCzRr-reW-XEbt-ic_gga6k8wkhwHo
"""

import pandas as pd
import matplotlib.pyplot as plt
query_df = pd.read_csv('/content/QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

query_df.DATE = pd.to_datetime(query_df.DATE)

query_df.head()

query_df.tail()

query_df.shape

query_df.count()

query_df.groupby('TAG').sum()

query_df.groupby('TAG').count()

reshaped_df = query_df.pivot(index='DATE', columns='TAG', values='POSTS')

reshaped_df.fillna(0, inplace=True)

reshaped_df.shape

reshaped_df.head()

reshaped_df.tail()

reshaped_df.count()

plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000) 

for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column], 
             linewidth=3, label=reshaped_df[column].name)

plt.legend(fontsize=16)

roll_df = reshaped_df.rolling(window=12).mean()
 
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
 
# plot the roll_df instead
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], 
             linewidth=3, label=roll_df[column].name)
 
plt.legend(fontsize=16)