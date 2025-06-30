import numpy as np
arr=np.array([[4,5,54],[6,7,7]])
new=np.insert(arr,1,[7,8,8],axis=None)
print(new)

arr=np.array([[4,5,54],[6,7,7]])
new=np.insert(arr,1,[7,8,8],axis=1)
print(new)