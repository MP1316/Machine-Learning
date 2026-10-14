import pandas as pd
from sklearn.model_selection import train_test_split

# Create dataset

data = pd.DataFrame({
    'Study_Hours' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Marks' : [10, 20, 15, 30, 50, 45, 35, 55, 60, 70]

})

# Input Features

x = data[['Study_Hours']]

# Target Value
y = data['Marks']

# Split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=100)

# Print results
print("X_Train\n", x_train)
print("X_Test\n", x_test)
print("Y_Train\n", y_train)
print("Y_Test\n", y_test)