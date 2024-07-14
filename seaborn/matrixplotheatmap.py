import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

tip=sns.load_dataset('tips')
print(tip.head())


df=tip.corr(numeric_only=True)
print(df)

sns.heatmap(df)
plt.show(block=True)

fl=sns.load_dataset('flights')
print(fl.head())

df=fl.pivot_table(values='passengers',index='month',columns='year',observed=True)

sns.heatmap(df)
plt.show(block=True)