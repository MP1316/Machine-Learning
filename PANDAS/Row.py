import pandas as pd
df = pd.read_json("sample_Data.json")
print("Display 10 row of first")
print(df.head(10))

print("Display 10 row of last")
print(df.tail(10))

