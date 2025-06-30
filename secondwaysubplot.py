import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,2,figsize=(10,10))
x=[1,2,3,4]
y=[10,20,15,30]
ax[0].plot(x,y)
ax[0].set_title("line chart")

ax[1].bar(x,y)
ax[1].set_title("bar")
#plt.tight_layout()
plt.show()