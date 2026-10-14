import matplotlib.pyplot as plt
# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
# sales = [1200, 1500, 1700, 2000, 2200, 2500]
# plt.plot(months, sales, marker='o', linestyle='--', color='b', linewidth=2, markersize=8, label='sales2025')
# plt.xlabel('Months')
# plt.ylabel('Sales')
# plt.title('Sales Data')
# plt.legend( loc='upper left')
# plt.grid(color='gray', linestyle=':', linewidth=1)
# plt.xlim('Jan', 'May')
# plt.ylim(0, 3000)
# # plt.xticks(['J', 'F', 'M', 'A', 'M'], [1200, 1500, 1700, 2000, 2200])      
# plt.show()

# Bar Chart
# plt.barh(months, sales, color='orange',  label='Sales 2025')
# plt.xlabel('Months')
# plt.ylabel('Sales')
# plt.title('Sales Data')
# plt.legend( loc='upper left')
# plt.show()  


# Pie Chart
# regions = ['North', 'South', 'East', 'West', 'Central']
# sales = [1200, 1500, 1700, 2000, 2200]
# plt.pie(sales, labels=regions, autopct='%1.1f%%', colors=['red', 'blue', 'green', 'yellow', 'purple'] )
# plt.title('Sales Data by Region')
# plt.show()


# Histogram
# marks =[45,67,78,89,56,72,90,66,55,92,74,68,59,85]
# plt.hist(marks, bins=5, color='blue', edgecolor='black')
# plt.xlabel('Marks')
# plt.ylabel('Frequency')
# plt.title('Histogram of Marks')
# plt.grid = plt.grid(color='gray', linestyle=':', linewidth=1)
# plt.show()

# Scatter Plot
height =[150, 160, 170, 180, 190, 200]
weight = [50, 60, 70, 80, 90, 100]
plt.scatter(height, weight, color='blue', marker='o')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Scatter Plot of Height vs Weight')
plt.grid(color='gray', linestyle=':', linewidth=1)
plt.show()
