import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
new_arr = np.delete(arr, 1, axis=0) #deleting row at index 1
print(new_arr)