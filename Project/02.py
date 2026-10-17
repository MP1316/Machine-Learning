import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("Project\student_performance_dataset.csv")
print(data.isnull().sum())

data = data.dropna()

# Input and Output 
x = data[["study_hours_per_day"]]
y = data["exam_score"]

# train model
model = LinearRegression()
model.fit(x, y)
predicted = model.predict(x)

# Evaluate model
MAE = mean_absolute_error(y, predicted)
MSE = mean_squared_error(y, predicted)
RMSE = np.sqrt(MSE)
r2 = r2_score(y, predicted)

# show evaluate model
print("Mean Absolute Error: ",round(MAE, 2))
print("Mean Squared Error: ",round(MSE, 2))
print("Root Mean Squared Error: ",round(RMSE, 2))
print("R^2 Score (Model Accuracy): ", round(r2, 4)) #closer to 1 = better


# Histogram
# plt.figure(figsize=(10,6))
# plt.hist(data["exam_score"], bins=20, color="red", edgecolor="black")
# plt.xlabel('Exam Score')
# plt.ylabel('Study Hours Per day')
# plt.title('Distribution Marks of Final Exam Score')
# # plt.grid(True)
# plt.show()      

# Scatter + Regression Line

plt.figure(figsize=(10,6))
plt.scatter(x, y, color="blue",label="Actual Score")
plt.plot(y, predicted, color="red", label="Predicted Score")
plt.xlabel('Study Hours Per day')
plt.ylabel('Final output')
plt.title('Model Prediction and Actual Prediction')
plt.legend()
plt.grid(True)
plt.show()      

hours = 9
predicted_new_score = model.predict([[hours]])
print(f"Predicted Final Score for {hours} hours is {predicted_new_score} score")