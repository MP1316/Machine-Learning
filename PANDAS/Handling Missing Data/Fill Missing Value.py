import pandas as pd
data = {
    "Name":["Mohit",None,"Chandan","Priayam","Piyush","Shalu"],
    "Age":[22,None,17,23,15,16],
    "Salary":[2000,None,50000,60000,30000,70000]
}
df = pd.DataFrame(data)
print(df)

# df.fillna(0, inplace=True)
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df)

