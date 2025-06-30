import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,15,30]
plt.plot(x,y)
plt.title("line chart")
plt.savefig('line_plot.png',dpi=300)
plt.show()