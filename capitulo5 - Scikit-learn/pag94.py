from sklearn import datasets
import pandas as pd

iris = datasets.load_iris()
df = pd.DataFrame(iris.data)

#print(iris.data)
#print(iris.feature_names)
#print(iris.target)
#print(iris.target_names)

print(df.head())