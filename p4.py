import matplotlib.pyplot as plt
Marks=[50,10,30,60,70,80,90,100]
plt.hist(Marks,bins=5,edgecolor="blue")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Histogram of Marks")
plt.show()