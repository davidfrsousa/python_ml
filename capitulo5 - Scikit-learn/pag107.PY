import pandas as pd
import numpy as np
from sklearn import preprocessing

#df = pd.read_csv('NaNDataset.csv')
#df.B = df.B.fillna(df.B.mean()) # fill all NaN columns with the mean
#df = df.dropna() # drop all rows with NaN values
#df = df.reset_index(drop=True) # reset the index after droping rows
#print(df)

#df2 = pd.read_csv('DuplicateRows.csv')
#print(df2[df2.duplicated(keep=False)])

#df2.drop_duplicates(keep='first', inplace=True) # drop duplicates and keep first
#df2.drop_duplicates(subset = ['A', 'C'],keep='first', inplace=True)
#df2 = df2.reset_index(drop=True)
#print(df2)

df = pd.read_csv('NormalizeColumns.csv')
x = df.values.astype(float)

min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
df = pd.DataFrame(x_scaled, columns=df.columns)
#print(df)

def outliers_iqr(data):
    q1, q3 = np.percentile(data, [25,75])
    iqr = q3 - q1
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    return np.where((data > upper_bound) | (data < lower_bound))

df2 = pd.read_csv('http://www.mosaic-web.org/go/datasets/galton.csv')

#print('Outliers using outliers_iqr()')
#print('=============================')
#for i in outliers_iqr(df2.height)[0]:
#    print(df2[i:i+1])


def outliers_z_score(data):
    threshold = 3
    std = np.std(data)
    mean = np.mean(data)
    z = [(y - mean)/std for y in data]
    return np.where(np.abs(z) > threshold)

print("Outliers using z score")
print('======================')
for i in outliers_z_score(df2.height)[0]:
    print(df2[i:i+1])