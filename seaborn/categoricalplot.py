import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df=sns.load_dataset('tips')
sns.barplot(x='sex',y='total_bill',data=df)
plt.show(block=True)

#countplot 
sns.countplot(x='sex',data=df)
plt.show(block=True)

sns.boxplot(x='sex',y='total_bill',data=df)
plt.show(block=True)