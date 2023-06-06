import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

"""
titanic = sns.load_dataset('titanic')
g = sns.catplot(x='who', y='survived', col='class',
data=titanic, kind = 'bar', ci=None, aspect = 1)

g.set_axis_labels('','Survival Rate')
g.set_xticklabels(['Men', 'Women','Children'])
g.set_titles('{col_name} {col_var}')

plt.show(block=True)

iris = sns.load_dataset('iris')
g = sns.lmplot(x='petal_width', y='petal_length',data=iris,
hue='species',palette='Set1',fit_reg=False,scatter_kws={'s': 70})

ax = plt.gca()
ax.set_title('Plotting using the Iris dataset')

plt.show(block=True)
"""

sns.set_style('whitegrid')

data = pd.read_csv('salary.csv')

sns.swarmplot(x='gender', y='salary', data=data)
ax = plt.gca()
ax.set_title('Salary Distribution')

plt.show(block=True)