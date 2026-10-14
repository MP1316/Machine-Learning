import pandas as pd
data = {
    "Name":["Mohit","Pinki","Chandan","Priayam","Piyush","Shalu"],
    "Age":[22,20,17,23,15,16],
    "Salary":[2000,10000,50000,60000,30000,70000]
}
df = pd.DataFrame(data)
print(df)
# print("Modified data")
# df.drop(columns=["Name"], inplace=True)
# print(df)

# multiple data removing
print("Multiple data removing")
df.drop(columns=["Name", "Salary"], inplace=True)
print(df)