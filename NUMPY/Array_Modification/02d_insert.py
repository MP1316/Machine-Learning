import numpy as np
arr = np.array([[1, 2], [ 5, 6]])
new_arr = np.insert(arr, 1, [11, 12], axis=None)  #inserting [10, 11, 12] at index 1
print(new_arr)
