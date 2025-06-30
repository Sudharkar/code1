import matplotlib.pyplot as plt
hours=[1,2,3]
marks=[50,55,60]
plt.scatter(hours,marks,color='red',label="class A sec")
hours1=[1,2,3]
marks1=[40,50,55]
plt.scatter(hours1,marks1,color='green',label="class B sec")

plt.xlabel("Study Hours")
plt.ylabel("Marks Obtain")
plt.title("Comparision of Two Classes")
plt.legend()
plt.show()