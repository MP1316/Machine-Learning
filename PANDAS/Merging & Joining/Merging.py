import pandas as pd
df_customers = pd.DataFrame({
    'CustomerID':[1,2,3],
    'Name':['Mohit','Rohan','Mohan']
})

df_order = pd.DataFrame({
    'CustomerID':[1,2,3],
    'Order Amount':[765,234,876]
})
df_merged = pd.merge(df_customers,df_order, on="CustomerID", how="inner")

print(df_merged)
