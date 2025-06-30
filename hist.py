import matplotlib.pyplot as plt
scores=[45,68,84,75,66,95,89,61,82,94,97,91,55,53,55,67,66]
plt.hist(scores,bins=5,color='purple',edgecolor='black')
plt.xlabel('score range',color="blue")
plt.ylabel("Number of student",color="blue")
plt.title("Score Distribution Of Student",color="orange")
plt.show()