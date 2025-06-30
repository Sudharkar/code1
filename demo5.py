import numpy as np

'''
a=np.array((23))
print(a)
print(type(a))
print(a.ndim)

a=np.array([1,2,3])
print(a)
print(type(a))
print(a.ndim)

a=np.array([[1,2,3],[4,5,6]])
print(a)
print(type(a))
print(a.ndim)
print(a[0,1])

a=np.array([[[1,2,5],[4,5,5]],[[44,55,66],[6,7,8]]])
print(a)
print(type(a))
print(a.dtype)
print(a[1,1,1])
print(a[-1,-1,-1])

a=np.arange(1,11)
print(a)

ar=np.array([1.,4.,5.,])
print(type(ar))
print(ar.ndim)
print(ar.min())
print(ar.max())
print(ar.sum())
print(ar.argmin())
print(ar.argmax())
print(a.dtype)

ar=np.array([1,2,3],dtype='i')
print(ar)
ar=np.array([1,2,3],dtype='f')
print(ar)
ar=np.array([1,2,3],dtype='U')
print(ar)

ar=np.array([1,2,3])
c=ar.copy()
c[0]=10
print(ar)
print(c)

ar=np.array([1,2,3])
v=ar.view()
v[0]=100
print(ar)
print(v)
'''

#sort array
ar=np.array([1,2,3,44,55,43,10])
s=np.sort(ar)
print(s)

ar=np.array([[1,3,2],[4,5,2]])
result=np.sort(ar)
print(result)

ar=np.array([[10,200,3200],[90,80,700]])
print(np.sort(ar,axis=0))

ar=np.array([[10,200,3200],[90,80,7000]])
print(np.sort(ar,axis=1))
print(ar.sum())
print(sum(ar))
print(ar.sum(axis=1))
print(ar.min())
print(ar.max())
print(ar.argmin())
print(ar.argmax())

ar=np.arange(1,10)
print(ar)

ar=np.ones((4,5),dtype='i')
print(ar)
print(np.any(ar==0))
print(np.all(ar==0))
print(ar[0,1])

ar=np.zeros((2,2),dtype='i')
print(ar)
print(ar.dtype)

ar=np.array([1,2,3])
ar2=np.array([2,3,4])
ar3=np.array([4,5,6])
print((ar<=ar2)&(ar2<=ar3).all())

ar=np.array([1,2,3])
print(np.shape(ar))

ar=np.array([[1,2,3],[3,4,5]])
print(np.shape(ar))

ar=np.array([[1,2],[3,4],[5,6],[7,8]])
print(np.shape(ar))

ar=np.array([1,2,3,3,34,4,4,5])
print(np.reshape(ar,(2,4)))
s=np.reshape(ar,(4,2))
print(s)

ar=np.full((3,3),200)
print(ar)

n=np.eye((3),dtype='i')
print(n)

ar=np.arange(1,100,2,dtype='f')
print(ar)


print(np.arange(1,10,2))

#linspace
a=np.linspace(1,20,5)
print(a)

a=np.linspace(1,10,5,endpoint=False)
print(a)

a=np.linspace(1,20,10,endpoint=True,retstep=True)
print(a)

a=np.linspace(1,10,3,endpoint=True,retstep=True)
print(a)

a=np.linspace(1,10,endpoint=False,retstep=True,dtype='i')
print(a)

a=np.array([1,2,3,2,3])
res=np.asarray(a,dtype='float',order='c')
print(res)
for i  in a:
    print(i)

a=np.array([[[[1,2,3],[4,65,67]]]])
for i in a:
    for j in i:
       for k in j:
          for n in k:
             print(n)
          print()
        
    print()
print()
print("radhe radhe")


a=np.array([[[[1,2,3],[4,65,67]],[[1,2,3],[4,65,67]]]])
for i in np.nditer(a):
    print(i)
    print()

a=np.array([[1,2,3],[4,65,67]])
l=len(a)
for i in range(l):
    for j in range(len(a[i])):
        print(a[i][j])

ar=np.array([1,23,3])
ar2=np.array([5,6,7])
ar3=np.concatenate((ar,ar2))
print(ar3)

ar=np.array([[1,23,3],[5,6,7]])
ar2=np.array([[5,6,7],[6,7,89]])
ar3=np.concatenate((ar,ar2))
print(ar3)


ar=np.array([[1,23,3],[5,6,7]])
ar2=np.array([[5,6,7],[6,7,89]])
ar3=np.concatenate((ar,ar2),axis=0)
print(ar3)

ar=np.array([[1,23,3],[5,6,7]])
ar2=np.array([[5,6,7],[6,7,89]])
ar3=np.concatenate((ar,ar2),axis=1)
print(ar3)


ar=np.array([1,23,3])
ar2=np.array([5,6,7])
ar3=np.stack((ar,ar2),axis=1)
print(ar3)

ar=np.array([1,23,3])
ar2=np.array([5,6,7])
ar3=np.vstack((ar,ar2))
print(ar3)

ar=np.array([1,23,3])
ar2=np.array([5,6,7])
ar3=np.hstack((ar,ar2))
print(ar3)


ar=np.array([1,23,3])
ar2=np.array([5,6,7])
ar3=np.dstack((ar,ar2))
print(ar3)

ar=np.array([2,3,434,5])
a=np.array_split(ar,2)
print(a)
a=np.array_split(ar,3)
print(a)

