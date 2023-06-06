from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#df = pd.read_csv('polynomial.csv')

#x = df.x[0:6, np.newaxis]
#y = df.y[0:6, np.newaxis]

#degree = 4
#polynomial_features = PolynomialFeatures(degree = degree)
#x_poly = polynomial_features.fit_transform(x)
#print(x_poly)
#print(polynomial_features.get_feature_names('x'))

#model = LinearRegression()
#model.fit(x_poly, y)
#y_poly_pred = model.predict(x_poly)

#plt.scatter(x, y, s=10)
#plt.plot(x, y_poly_pred)

#print(model.intercept_)
#print(model.coef_)

dataset = load_boston()
df = pd.DataFrame(dataset.data,columns=dataset.feature_names)
df['MEDV'] = dataset.target

x = pd.DataFrame(np.c_[df['LSTAT'], df['RM']], columns=['LSTAT','RM'])
Y = df['MEDV']

x_train, x_test, Y_train, Y_test = train_test_split(x, Y,
 test_size= .3,random_state=5)

degree = 2
polynomial_features = PolynomialFeatures(degree= degree)
x_train_poly = polynomial_features.fit_transform(x_train)

model = LinearRegression()
model.fit(x_train_poly, Y_train)

x_test_poly = polynomial_features.fit_transform(x_test)
print('R²: %.4f' % model.score(x_test_poly, Y_test))

fig = plt.figure(figsize=(18,15))
ax = fig.add_subplot(111,projection='3d')

ax.scatter(x['LSTAT'], x['RM'], Y, c='b')
ax.set_xlabel('LSTAT')
ax.set_ylabel('RM')
ax.set_zlabel('MEDV')

x_surf = np.arange(0,40,1)
y_surf = np.arange(0,10,1)
x_surf, y_surf = np.meshgrid(x_surf,y_surf)

x_poly = polynomial_features.fit_transform(x)
model.fit(x_poly,Y)

z = lambda x,y: (model.intercept_+
model.coef_[1]*x+model.coef_[2]* y+
model.coef_[3]* x**2+ model.coef_[4] * x*y+
model.coef_[5] * y**2)

ax.plot_surface(x_surf, y_surf, z(x_surf,y_surf),
rstride= 1,
cstride = 1,
color ='None',
alpha = .4)

plt.show(block=True)