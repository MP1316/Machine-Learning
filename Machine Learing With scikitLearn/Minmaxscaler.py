import pandas as pd 
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

data = pd.DataFrame({
    'age' :[10, 20, 30],
    'salary' : [5000, 10000, 15000]
})

minmaxscaler  = MinMaxScaler()

minmax_data = minmaxscaler.fit_transform(data)
print("MinMaxScaler Data :")
print(pd.DataFrame(minmax_data, columns=['age', 'salary']))
print(minmax_data)

