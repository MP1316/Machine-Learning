# Data for the bar chart
import matplotlib.pyplot as plt
students = ['Rahul','Aman','Ravi','Sita','Anjali']
marks = [85, 90, 78, 92, 88]
plt.barh(students, marks, color='orange', label='Marks')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.title('Student Marks')
plt.legend()
plt.show()
