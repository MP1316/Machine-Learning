import pandas as pd
# df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
# print(df.info())
data = {
    "Name":["Mohit", "Pinki", "M16"],
    "Age":[98,76,54],
    "City":["Delhi","Mumbai","Jaipur"]
}
df = pd.DataFrame(data)
print(df.info())