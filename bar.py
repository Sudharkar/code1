import matplotlib.pyplot as plt
product=['A','B','C','D']
sales=[1000,1500,800,1200]
plt.bar(product,sales,color='red',label='Sales Record 2024')
plt.xlabel("product Name")
plt.ylabel("Sales Product")
plt.legend()
plt.title("Salling Product In 2024")

plt.show()