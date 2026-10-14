import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    'name' : ['mohit', 'rohit', 'riya', 'priya', 'rohan', 'priyanka'],
    'gender' : ['male', 'male', 'female', 'female', 'male', 'female'],
    'passed' : ['yes', 'no', 'no', 'yes', 'yes', 'no']
}

df = pd.DataFrame(data)

one_hot_encoding = pd.get_dummies(df,  dtype=int)
# one_hot_encoding = pd.get_dummies(df, columns=['name', 'gender'])
print(one_hot_encoding) 

