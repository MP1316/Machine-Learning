from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Actual data
x_true = [0, 1, 0, 1, 0, 1, 0]

# Prediction data
y_predict = [0, 1, 0, 1, 1, 0, 0]

print("Accuracy: ", accuracy_score(x_true, y_predict))
print("Precission: ", precision_score(x_true, y_predict))
print("Recall: ", recall_score(x_true, y_predict))
print("F1 Score: ", f1_score(x_true, y_predict))