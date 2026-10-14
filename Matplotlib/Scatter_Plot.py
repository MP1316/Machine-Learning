import matplotlib.pyplot as plt
hours =[1, 2, 3, 4, 5, 6, 7]
marks =[50,55,60,65,70,75,80]
plt.scatter(hours, marks, color='red', marker='o', label='Marks vs Hours')
plt.xlabel('Hours')
plt.ylabel('Marks')
plt.title('Scatter Plot of Marks vs Hours')
plt.legend()
plt.grid(color='gray', linestyle=':', linewidth=1)
plt.show()