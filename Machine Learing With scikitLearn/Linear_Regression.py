from sklearn.linear_model import LinearRegression
import pandas as pd

x = [[1], [2], [3], [4], [5]]
y = [20, 30, 40, 50, 60]

model = LinearRegression()
model.fit(x, y)

hours = int(input("Enter you hours study:"))
prediction = model.predict([[hours]])

print(prediction)