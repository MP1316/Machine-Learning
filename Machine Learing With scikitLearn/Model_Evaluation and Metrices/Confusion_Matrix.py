from sklearn.metrics import confusion_matrix
import pandas as pd

# actual_value
actual_value = [1, 0, 1, 1, 0, 1, 0]

# Prediction value
predict_value = [1, 0, 1, 1, 1, 0, 1]


print("Confusion Matrix:\n ", confusion_matrix(actual_value, predict_value))
