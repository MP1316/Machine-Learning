# Data for the bar chart
import matplotlib.pyplot as plt
subjects = ['python', 'numpy', 'pandas', 'matplotlib', 'ml']
num_of_students = [40, 35, 30, 25, 20]
plt.bar(subjects, num_of_students, color='green', label='No. of Students')
plt.title("Number of Students in Each Subject")
plt.xlabel("Subjects")
plt.ylabel("Number of Students")
plt.legend(loc='upper right', linewidth=1)
plt.show()

