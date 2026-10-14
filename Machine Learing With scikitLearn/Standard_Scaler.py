import pandas as pd 
from sklearn.preprocessing import StandardScaler

data = pd.DataFrame({
    'age' :[10, 20, 30],
    'salary' : [5000, 10000, 15000]
})

scaler = StandardScaler()

scalered_data = scaler.fit_transform(data)
print("Scaled Data :")
print(pd.DataFrame(scalered_data))
