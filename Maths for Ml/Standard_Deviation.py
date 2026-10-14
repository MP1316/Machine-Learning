import numpy as np
import matplotlib.pyplot as plt
data = np.array([2,4,6,8])
# data_02 = 800
# # print(np.mean(arr))

# # Varience

print("Varience", np.var(data))   
print("Standard_Deviation", np.std(data))
# print("Standard_Deviation", np.sqrt(data_02))

# Bar graph

'''

y = [10,20,30,40]
x = ["hindi","math","science","bio"]
plt.bar(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("categorical data")
plt.show()

'''

# Histogram

"""

x = [10,20,30,40,20,10,30,40,50]
# y = [1,2,3,4]
plt.hist(x, bins=3)
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.title("Students Data")
plt.show()

"""