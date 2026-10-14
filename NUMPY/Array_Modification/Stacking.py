import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
result = np.vstack([arr[0], arr[1]])
print(result)
result = np.hstack([arr[0], arr[1]])
print(result)