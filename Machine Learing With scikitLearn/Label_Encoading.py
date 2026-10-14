import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    'name' : ['mohit', 'rohit', 'riya', 'priya', 'rohan', 'priyanka'],
    'gender' : ['male', 'male', 'female', 'female', 'male', 'female'],
    'passed' : ['yes', 'no', 'no', 'yes', 'yes', 'no']
}

df = pd.DataFrame(data)
# df_label = df.copy()
le = LabelEncoder()

df['gender_encoded'] = le.fit_transform(df['gender'])
df['passed_encoded'] = le.fit_transform(df['passed'])

print('\nLabel Encoded:')
print(df)
# print(df[['name', 'gender', 'gender_encoded', 'passed', 'passed_encoded']])

