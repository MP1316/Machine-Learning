import numpy as np
arr = np.array([32, np.nan, 45, 67, np.nan])
print(np.isnan(arr))    
result = np.nan_to_num(arr , nan=51)  # Replace NaN with 51
print(result)
