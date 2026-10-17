import pandas as pd
data = {
    "Hours" : [1, 2, 3, 4, 5],
    "Marks" : [52, 57, 70, 75, 80]
}

df = pd.DataFrame(data)
df.to_csv("Student_Data.csv", index=False)
