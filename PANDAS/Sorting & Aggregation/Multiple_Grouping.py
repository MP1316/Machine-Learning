import pandas as pd
data = {
    "Name":['Mohit','Pinki','Rohan','Mohan','Chotu   '],
    "Age":[17,23,17,23,15],
    "Salary":[2000,10000,50000,60000,30000]
}
df = pd.DataFrame(data)
print(df)

grouped = df.groupby(["Name", "Age"])["Salary"].sum()
print(grouped)