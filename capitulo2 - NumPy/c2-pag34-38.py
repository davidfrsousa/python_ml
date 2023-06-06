import numpy as np

list1 = [[1,2,3,4],[5,6,7,8]]
a1 = np.array(list1)

#a2 = a1 #copy by reference: all changes affect original
#a2 = a1.view() #copy by view (shallow copy): only changes in shape doesn't affect original

a2 = a1.copy() #copy by value (deep copy): any changes won't affect original
a1[0][0] = 11
a1.shape = 1, -1
print(a1)
print(a2)