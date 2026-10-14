import matplotlib.pyplot as plt
plt.scatter([1, 2, 3, 4, 5], [50, 55, 60, 65, 70], color='blue', marker='o', label='Marks vs Hours(Group 1)')
plt.scatter([1, 2, 3, 4, 5], [60, 65, 70, 75, 80], color='red', marker='^', label='Marks vs Hours (Group 2)')
plt.xlabel('Hours')    
plt.ylabel('Marks')
plt.title('Scatter Plot of marks vs Hours')
plt.legend()
plt.grid(color='gray', linestyle=':', linewidth=1)
plt.show()