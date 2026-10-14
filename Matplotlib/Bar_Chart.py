import matplotlib.pyplot as plt
months = ['M1', 'M2', 'M3', 'M4', 'M5']
sales = [500, 1500, 1000, 2000, 2500]
plt.barh(months, sales, color='blue', label='Sales 2025')
plt.title("Monthly Sales Data")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend(loc='upper left', linewidth=1)
plt.show()
