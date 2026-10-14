import pandas as pd
data = {
    "Age":[22,20,22,20,15],
    "Salary":[20000,30000,70000,50000,60000]
}
df = pd.DataFrame(data)
print(df)

grouping = df.groupby("Age")["Salary"].sum()
print("After Grouping")
print(grouping)

"""
df.groupby("Age")
age = 22 [20000,70000]
age = 20[30000,50000] 
age = 15[60000] 

["Salary].sum()

age = 22 [20000,70000] = 90000
age = 20[30000,50000] = 80000
age = 15[60000] = 60000

"""