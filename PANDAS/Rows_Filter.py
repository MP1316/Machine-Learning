import pandas as pd
data = {
    "Name":["Mohit","Pinki","Chandan","Priayam","Piyush","Shalu"],
    "Age":[22,20,17,23,15,16],
    "Salary":[2000,10000,50000,60000,30000,70000]
}
df = pd.DataFrame(data)
# high_salary = df[df['Salary']>5000]
# print('if salary is greater than 5000')
# print(high_salary)

filtered = df[df(['Salary'] > 5000 ) & (df['Age'] < 18)]
print(filtered)
