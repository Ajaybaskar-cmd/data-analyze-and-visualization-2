import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=sns.load_dataset('tips')
print(df.head())

sns.displot(df['total_bill'])
plt.show(block=True)

#create the joint plot
sns.jointplot(x='total_bill',y='tip',data=df)
plt.show(block=True)

sns.jointplot(x='total_bill',y='tip',data=df,kind='hex')
plt.show(block=True)

sns.rugplot(df['total_bill'])
sns.kdeplot(df['total_bill'])
plt.show(block=True)