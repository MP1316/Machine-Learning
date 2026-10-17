import matplotlib.pyplot as plt
marks = [55, 70, 65, 80, 90, 75, 85, 60, 95, 50, 40, 45]
plt.hist(marks, bins=7, color='green', edgecolor='black', alpha=0.7)
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.title('Histogram of Marks')
plt.show()      