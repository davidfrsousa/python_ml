import numpy as np

#x1 = np.array([[1,2,3],[4,5,6]])
#y1 = np.array([[7,8,9],[2,3,4]])
#print(x1 * y1)

x = np.array([2,3])
y = np.array([4,2])
#z = x + y
#print(z)
print(np.dot(x,y)) #dot product is different than multiply for arrays

x2 = np.array([[1,2,3],[4,5,6]])
y2 = np.array([[7,8],[9,10],[11,12]])
print(np.dot(x2,y2))

names = np.array(['David', 'Sheila', 'Solange'])
#heights = np.array([1.73,1.74,1.63])
weights = np.array([63,82,70])

#bmi = weights/heights**2
#print(bmi)

#print('Overweight: ', names[bmi>25])
#print('Underweight: ', names[bmi<18.5])
#print('Healthy: ', names[(bmi<25) & (bmi>18.5)])

#x3 = np.matrix([[1,2],[4,5]])
#y3 = np.matrix([[7,8],[2,3]])

x1 = np.array([[1,2],[4,5]])
y1 = np.array([[7,8],[2,3]])
x3 = np.asmatrix(x1) #matrix always 2-dimensional
y3 = np.asmatrix(y1)
print(x1 * y1) #matrix is always dot product
print(x3 * y3)

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a.cumsum(axis=1)) #axis = 0 to column, 1 to row

ages = np.array([34,12,37,5,13])
#ages.sort()
#sorted_ages = np.sort(ages)
#print(ages[ages.argsort()])

persons = np.array(['Johnny', 'Mary', 'Peter', 'Will', 'Joe'])
heights = np.array([1.76,1.2,1.68,0.5,1.25])
sort_indices = np.argsort(persons)[::-1] #[::-1] is to reverse the order
print(persons[sort_indices]) #argsort returns the indices in order
print(ages[sort_indices])
print(heights[sort_indices])