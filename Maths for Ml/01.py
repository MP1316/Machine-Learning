# Plotting Graphs using Matplotlib by linear equations
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = []
for i in x:
    y.append(2 * i + 10)  # Linear equation y = 2x + 10
plt.plot(x, y, label='y = 2x + 10', color='blue', marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Graph')
plt.legend()
plt.show()
