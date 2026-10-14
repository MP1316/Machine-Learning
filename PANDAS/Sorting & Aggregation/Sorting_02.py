import pandas as pd
data = {
    # "Name":["Mohit","Pinki","Chandan","Priayam","Piyush","Shalu"],
    "Age":[22,20,17,23,15,16],
    "Salary":[20000,30000,70000,50000,60000,40000]
}
df = pd.DataFrame(data)
print(df)
print("Before Sorting")

df.sort_values(by=["Age", "Salary"], ascending=[True, True], inplace=True)
print("After sorting")

print(df)
