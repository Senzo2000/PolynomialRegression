import numpy as np
import matplotlib.pyplot as plt

# X will representing the years
X = [2, 4, 6, 8, 10, 75]
#Y will be representing the SALARIES of java developers
Y = [22, 37, 50, 66, 90, 100]

# Train Algorithm (Polynomial)
# 2 is the degree
poly_fit = np.poly1d(np.polyfit(X,Y, 2))

# Plotting of data
xx = np.linspace(0, 26, 100)
#The colour of the line will be red
plt.plot(xx, poly_fit(xx), c='r',linestyle='-')
#This is the heading of the graph
plt.title('JAVA DEVELOPER SALARY')
plt.xlabel('YEARS')
plt.ylabel('SALARY')
plt.axis([0, 25, 0, 100])
plt.grid(True)
plt.scatter(X, Y)
plt.show()

# Predict price


#REFERENCE OF X AND Y PLOT IN OFFERZEN.COM java developer salary.