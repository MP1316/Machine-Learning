import numpy as np
arr = np.array([10,20,30,40,50])
# mask = arr > 10
mask = (arr > 10) & (arr < 50)
print(arr[mask])
print(mask)