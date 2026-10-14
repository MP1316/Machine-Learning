import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
new_arr = np.insert(arr, 4, 90, axis=None)  #inserting 90 at index 4
print(new_arr)