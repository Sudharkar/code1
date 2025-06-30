import matplotlib.pyplot as plt
regions=['North','South','East','West']
revanue=[1000,3000,200,1500]
plt.pie(revanue,labels=regions,autopct='%1.1f%%',colors=['red','green','coral','lightgreen'])
plt.title('revanue condition by region')
plt.show()