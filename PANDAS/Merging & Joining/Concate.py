import pandas as pd
df_customers = pd.DataFrame({
    'CustomerID':[1,2],
    'Name':['Mohit','Rohan']
})

df_order = pd.DataFrame({
    'customerID':[3,4],
    'Name':['Sohit','Shyam']
})

df_concate = pd.concat([df_customers, df_order] , axis=1,ignore_index=True)
print(df_concate)