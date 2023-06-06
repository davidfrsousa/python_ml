# Generating datasets

import matplotlib.pyplot as plt
import numpy as np
import pickle
from sklearn.datasets._samples_generator import make_regression
from sklearn.datasets._samples_generator import make_blobs
from sklearn.datasets._samples_generator import make_circles
from sklearn.linear_model import LinearRegression
import joblib

"""
x, y = make_regression(n_samples=100, n_features=1, noise=5.4)
plt.scatter(x,y)

plt.show(block=True)
"""
"""
X, y = make_blobs(500, centers = 3)

rgb = np.array(['r','g','b'])
plt.scatter(X[ : ,0], X[ : ,1], color=rgb[y])

plt.show(block=True)
"""
#X,y = make_circles(n_samples=100, noise= .09)
#rgb = np.array(['r','g','b'])

#plt.scatter(X[ : ,0], X[ : ,1], color=rgb[y])
#plt.show(block=True)

heights = [[1.6],[1.65],[1.7],[1.73],[1.8]]
weights = [[60],[65],[72.3],[75],[80]]

#model = LinearRegression()
#model.fit(X=heights, y=weights)

plt.title('Weights plotted against heights')
plt.xlabel('Heights in meters')
plt.ylabel('Weights in kg')

plt.plot(heights, weights, 'b.')

plt.axis([1.5,1.85,50,90])
plt.grid(True)

#plt.plot(heights, model.predict(heights), 'r')

#print(round(model.intercept_[0],2))
#print(round(model.coef_[0][0],2))

#print('Residual sum of squares(RSS): %.2f' %
#    np.sum((weights-model.predict(heights)) ** 2))

#plt.show(block=True)

######### TEST DATA ########

heights_test = [[1.58],[1.62],[1.69],[1.76],[1.82]]
weights_test = [[58],[63],[72],[73],[85]]

#weights_test_mean = np.mean(np.ravel(weights_test))
#tss = np.sum(np.ravel((weights_test - weights_test_mean) ** 2))
#rss = np.sum(np.ravel((weights_test - model.predict(heights_test)) ** 2))
#r2 = 1 - (rss/tss)

#print('%.4f'%model.score(heights_test,weights_test))
#print('R²: %.4f' % r2)

filename = 'HeightsAndWeights_model2.sav'
#pickle.dump(model, open(filename, 'wb'))

#loaded_model = pickle.load(open(filename,'rb'))

#result = loaded_model.score(heights_test,weights_test)

#joblib.dump(model, filename)

loaded_model = joblib.load(filename)
result = loaded_model.score(heights_test,weights_test)
print(result)