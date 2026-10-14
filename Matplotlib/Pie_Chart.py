import matplotlib.pyplot as plt
regions = ['North', 'South', 'East', 'West']
sales = [1500, 2000, 1800, 2200]
plt.pie(sales, labels=regions, autopct='%1.1f%%',
         colors=['#ff9999','#66b3ff','#99ff99','#ffcc99']  )
plt.title("Sales Distribution by Region")
plt.show()  