import matplotlib.pyplot as plt
months = [1, 2, 3, 4, 5, 6]
sales = [200, 250, 300, 400, 350, 500]
plt.plot(months, sales, color='blue', marker='o',
          linestyle='--', linewidth=2, label='Sales')

plt.title("Monthly Sales Data")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend(loc='lower right', linewidth=2)
plt.grid(color='gray', linestyle=':', linewidth=1)
plt.xlim(0, 5)
plt.ylim(0, 400)
plt.xticks([1, 2, 3, 4], ['M1', 'M2', 'M3', 'M4'])
plt.show()

  