# Data for the line plot
import matplotlib.pyplot as plt
weeks = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
hours = [5,6,4,7,6,8,5]
plt.plot(weeks, hours, color='purple', marker='o', linestyle='--', 
         linewidth=2, label='Hours Spent')
plt.xlabel('Weeks')
plt.ylabel('Hours')
plt.title('Weekly Study Hours')
plt.legend()
plt.show()  
