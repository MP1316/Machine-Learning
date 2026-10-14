import pandas as pd 
data = {
    "name" : ["mohit", "rohan", "ravi", "sachin", "manish"],
    "age" : [None, 23, 65, None, 34],
    "salary" : [30000, None, 40000, 20000, None]

}

df = pd.DataFrame(data)
print("Original data :")
print(df)

print(df.isnull().sum())
df_drop = df.dropna()
print(df_drop)

df["age"] = df["age"].fillna(df["age"].mean())
df["salary"] = df["salary"].fillna(df["salary"].mean())
print(df)
