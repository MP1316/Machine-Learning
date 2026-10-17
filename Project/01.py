import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Read csv file
data = pd.read_csv("Student_Data.csv")

# Input and Output
x = data[["Hours"]]
y = data["Marks"]

# Create and train model
model = LinearRegression()
model.fit(x, y)

# Predict on existing data
predicted = model.predict(x)

# Evaluate model
MAE = mean_absolute_error(y, predicted)
MSE = mean_squared_error(y, predicted)
RMSE = np.sqrt(MSE)

print("Mean Absolute Error: ", MAE)
print("Mean Squared Error: ", MSE)
print("Root Mean Squared Error: ", RMSE)

# Predict for seven hours study
new_hour = float(input("Enter hours: "))
new_predict = model.predict([[new_hour]])
print("Predicted marks for hours study: ", new_predict)
 