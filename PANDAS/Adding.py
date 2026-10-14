import pandas as pd
data = {
    "Name":["Mohit","Pinki","Chandan","Priayam","Piyush","Shalu"],
    "Age":[22,20,17,23,15,16],
    "Salary":[2000,10000,50000,60000,30000,70000]
}
df = pd.DataFrame(data)       
print(df)
df.insert(1, "employ id" , [9,8,7,6,5,3])
print(df)                    