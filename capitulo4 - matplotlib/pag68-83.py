import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('drivinglicense.csv')
g = sns.catplot(x='gender', y='license', col='group',
data=data, kind='bar', ci= None, aspect= 1.0)

g.set_axis_labels("",'Proportion with Driving license')
g.set_xticklabels(['Men', 'Women'])
g.set_titles('{col_var} {col_name}')

plt.show(block=True)