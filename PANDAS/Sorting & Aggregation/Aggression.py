import pandas as pd
data = {
    "Age":[22,20,17,23,15,16],
    "Salary":[20000,30000,70000,50000,60000,40000]
}
df = pd.DataFrame(data)
print(df)

avg_value = df["Age"].mean()
print(avg_value)