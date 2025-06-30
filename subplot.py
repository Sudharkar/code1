import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,15,30]
plt.subplot(1,2,2)
plt.plot(x,y,marker='o')
plt.title("Line Chart")

plt.subplot(1,2,1)
plt.bar(x,y)
plt.title("bar chart")
plt.tight_layout()
plt.show()