import pandas as pd
data = {
    "Name":["Mohit","Pinki","Chandan","Priayam","Piyush","Shalu"],
    "Age":[22,20,17,23,15,16],
    "Salary":[2000,10000,50000,60000,30000,70000]
}
data_frame = pd.DataFrame(data)
print("Describe data frame")
print(data_frame)
print("Descriptive Statistics")
print(data_frame.describe())
