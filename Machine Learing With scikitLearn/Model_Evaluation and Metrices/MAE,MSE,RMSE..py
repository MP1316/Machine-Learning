from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error

# Actual marks of the student
actual_marks = [80, 60, 90]

# Prediction marks of the students
predict_marks = [75, 65, 80]

print("MAE: ",mean_absolute_error(actual_marks, predict_marks))
print("MSE: ",mean_squared_error(actual_marks, predict_marks))
print("RMSE: ",root_mean_squared_error(actual_marks, predict_marks))