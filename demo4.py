
import numpy as np
'''
arr=np.array([[3,4,5],[5,67,7]])
print(arr)
print(type(arr))
print(np.__version__)
ar=np.array([1,2,3,3,5])
print(ar)
print(type(ar))
ar=np.array(4)
print(ar)
print(ar.ndim)
print(arr.ndim)
ar2=np.array([[[[1,2,3],[3,4,5]],[[7,8,98],[5,6,7]]]])
print(ar2)
print(ar2.ndim)
arr=np.array(([3,4,5,5]),ndmin=3)
print(arr)
print(ar2[0])
print(ar2[0][0])
print(ar2[0][0][0][2])
print(ar2[0][1][1])
print(ar2[0,1,1,1]+ar2[0,1,1,1])
print(ar2[:])
print(ar2[0][0][0][0:2:2])
arr=np.array([[3,4,5],[5,67,7]])
print(arr[0:2,1])
print(arr[0])
print(arr[0::,0:2])
arr=np.array(["apple","mango"])
print(type(arr.dtype))
arr=np.array([3,4,5])
print(type(arr.dtype))


arr=np.array([1,2,3,4])
x=arr.copy()
arr[1]=10
print(x)
print(arr)

arr=np.array([1,2,3,3])
print(arr)
x=arr.copy()
x[1]=22
print(x)
print(arr)


arr=np.array([1.2,3.4,45.5])
print(arr)
x=arr.view()
arr[2]=9.0
print(x)
print(arr)


arr=np.array([2,3,4,5])
x=arr.view()
x[1]=10
print(x)
print(arr)


arr=np.array([3,4,5],ndmin=4)
print(arr)
print(arr.ndim)
print(type(arr.dtype))


arr=np.array([[[[1,2,3,4,5,6],[4,5,65,6,7,8]]]])
print(arr.shape)
arr1=np.array([2,3,3,4,5,5],ndmin=4)
print(arr1)
print(arr1.shape)
arr1=np.array([2,3,3,4,5,5])
print(arr1.reshape(3,2))
print(arr1.reshape(2,3))
arr1=np.array([1,2,3,3,4,6,7,6,5,54,9,8])
print(arr1.reshape(3,2,2))
print(arr1.base)
'''
print("hello")

