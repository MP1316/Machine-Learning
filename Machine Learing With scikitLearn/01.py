import pandas as pd
data = {
    'Brand': ['Tatasiera', 'Defender', 'Xuv', 'Bolero', 'Fortuner'],
    'Price': [500000, None, 900000, 600000, 400000],
    'Average': [10, None, 50, None, 15],
    'Model' : [1999, 1995, 2003, 2000, None],
    'Seater' : [3, None, 5, None, 6]
}

df = pd.DataFrame(data)
print("Original Dataframe :")
print(df)

is_null = df.isnull().sum()
print(is_null)

# dropna = df.dropna()
# print(dropna)

df['Price'] = df['Price'].fillna(df['Price'].mean())
df['Average'] = df['Price'].fillna(df['Average'].mean())
df['Model'] = df['Model'].fillna(df['Model'].mean())
df['Seater'] = df['Seater'].fillna(df['Seater'].mean())
print(df)
