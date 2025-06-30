import numpy as np
'''
arr=np.array([3,4,5,5443,3])
new=np.delete(arr,2,axis=None)
print(new)

# with 2D array

arr=np.array([[4,6,7],[7,65,5]])
new=np.delete(arr,0,axis=0)
print(new)
'''

from numpy import random
#import random
#print(random.random())
#print(random.randint(100))
#print(random.rand())
#print(random.randrange(1,20))

ar=np.array([4,5,6,7])
print(random.choice(ar,size=(2,3)))