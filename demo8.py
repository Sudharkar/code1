import matplotlib.pyplot as plt
month=[1,2,3,4]
sales=[3000,4000,5000,6000]
plt.plot(month,sales,marker='s',linewidth=2,linestyle='solid',color='coral',label='sales data 2025')
plt.xlabel("month",color='blue')
plt.ylabel("sales according to month",color='blue')
plt.title("Monthy Sales Data",color='black')
plt.legend()
#plt.xlim(0,10)
#plt.ylim(1000,8000)
plt.grid(True)
plt.xticks([1,2,3,4],['m1','m2','m3','m4'])
plt.show()