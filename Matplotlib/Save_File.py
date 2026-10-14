import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [5,10,20,15,25]
plt.plot(x,y, color = 'blue', marker='o')
plt.title('Simple Line graph')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.savefig('Line_Plot.png', dpi=300, bbox_inches='tight')
plt.show() 