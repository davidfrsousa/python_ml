import numpy as np

a1 = np.arange(10)
print(a1)
print(a1.shape)

a2 = np.arange(0,10,2)
print(a2)

a3 = np.zeros(5)
print(a3)
print(a3.shape)

a4 = np.zeros((2,3))
print(a4)
print(a4.shape)

a5 = np.full((2,3), 8)
print(a5)

a6 = np.eye(4)
print(a6)

a7 = np.random.random((2,4)) # random between 0.0 and 1.0
print(a7)

list1 = [1,2,3,4,5]
r1 = np.array(list1)
print(r1)

print(r1[0])
print(r1[1])

list2 = [6,7,8,9,0]
r2 = np.array([list2,list1])
print(r2)
print(r2.shape)
print(r2[0,0])
print(r2[0,1])
print(r2[1,0])

print(r1[[2,4]]) # values in interval given
print(r1>2) # boolean values for all indices
print(r1[r1>2]) # only values in indices which boolean is True

nums = np.arange(20)
print(nums)
odd_num = nums[nums % 2 == 1]
print(odd_num)

a = np.array([[1,2,3,4,5],
              [4,5,6,7,8],
              [9,8,7,6,5]])
print(a)

b1 = a[1:3, :3]
print(b1)

b2 = a[-2:,-2:]
print(b2)

b3 = a[1:, 2:]
print(b3)

b4 = a[2:, :]
print(b4)
print(b4.shape)

b5 = a[2, :]
print(b5)
print(b5.shape)

b5 = b5.reshape(1,-1)
print(b5)

b4 = b4.reshape(-1,)
print(b4)