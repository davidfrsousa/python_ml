import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

dataset = load_boston()

df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
df['MEDV'] = dataset.target
#df.info() # check data type of each column
# if there is any non number value it needs to be encoded into numeric value

#print(df.isnull().sum())

#corr = df.corr() # return the correlation of columns

#### Print the 6 features which have higher correlation with the target
#print(df.corr().abs().nlargest(6, 'MEDV').index)
#print(df.corr().abs().nlargest(6, 'MEDV').values[:,13])

x = pd.DataFrame(np.c_[df['LSTAT'], df['RM']], columns=['LSTAT', 'RM'])
Y = df['MEDV']

fig = plt.figure(figsize=(18,15))
ax = fig.add_subplot(111,projection='3d')

ax.scatter(df['LSTAT'], df['RM'], df['MEDV'],c='b')
ax.set_xlabel('LSTAT')
ax.set_ylabel('RM')
ax.set_zlabel('MEDV')

x_surf = np.arange(0,40,1) # Grid for LSTAT
y_surf = np.arange(0,10,1) # Grid for RM
x_surf, y_surf = np.meshgrid(x_surf,y_surf)

x_train, x_test, Y_train, Y_test = train_test_split(x, Y, test_size=.3, random_state=5)

model = LinearRegression()
#model.fit(x_train, Y_train)
model.fit(x, Y)

#price_pred = model.predict(x_test)
z = lambda x,y: (model.intercept_ + model.coef_[0]*x + model.coef_[1]* y)

ax.plot_surface(x_surf,y_surf,z(x_surf,y_surf),
rstride = 1,
cstride = 1,
color = 'r',
alpha = .4)

#mse = mean_squared_error(Y_test,price_pred)
#print(mse)
#print('R²: %.4f' % model.score(x_test,Y_test))

#plt.scatter(Y_test, price_pred)
#plt.xlabel('Actual Prices')
#plt.ylabel('Predicted Prices')
#plt.title('Actual Prices vs Predicted Pices')

#print(model.intercept_) # print the interception with y axis
#print(model.coef_) # print the Beta coeficients

plt.show(block=True)