import numpy as np
arr = np.array([32, np.inf, 45, 67, -np.inf])
print(np.isinf(arr))

result = np.nan_to_num(arr, posinf=100, neginf=0)
print(result)