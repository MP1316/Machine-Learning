import matplotlib.pyplot as plt
# Data for the pie chart
# subjects = ['Python', 'NumPy', 'Pandas', 'other', 'Machine Learning']
# study_time = [40, 25, 10, 10, 10]
# plt.pie(study_time, labels=subjects, autopct='%1.1f%%', colors=['#ff9999','#66b3ff',
#                                                                 '#99ff99','#ffcc99', '#c2c2f0'])
# plt.title("Study Time Distribution by Subject")
# plt.show()


investment_types = ['Food', 'Travel', 'Education', 'Shopping', 'Savings']
monthly_budget= [500, 300, 200, 400, 600]
plt.pie(monthly_budget, labels=investment_types, autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0'])
plt.title("Monthly Budget Distribution")
plt.show()