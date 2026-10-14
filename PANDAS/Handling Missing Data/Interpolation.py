import pandas as pd
data = {
    "valve" : [10, None, 30, None, 50],
    "time" : [1,2,3,4,5]
}
df = pd.DataFrame(data)
print("Before interpolation")
print(df)

df['valve'] = df["valve"].interpolate(method="linear")
print("After linear")
print(df)