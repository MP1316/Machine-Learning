import pandas as pd
data = {
    "Name":["Mohit", "Pinki", "M16"],
    "Age":[98,76,54],
    "City":["Delhi","Mumbai","Jaipur"]
}
df = pd.DataFrame(data)
print(df)

# df.to_csv("Output.csv", index=False)
# df.to_json("Output.json", index=False)
df.to_excel("Output.xlsx", index=False)

