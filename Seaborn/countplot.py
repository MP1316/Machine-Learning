import seaborn as sns
import matplotlib.pyplot as plt

# daa = sns.load_dataset("titanic")
# sns.countplot(data=daa, x="class")  
# plt.show()


"""
# Load data from seaborn's built-in dataset
# total_bill, tip, sex, smoker, day, time, size 

data = sns.load_dataset("tips")
print(data.head())
sns.countplot(data=data, x="day")
plt.show()

"""
data = {
    "day": ["Thur", "Sat", "Sun", "Mon", "Fri", "Tue", "Wed"],
    "total_bill": [20.53, 10.34, 23.68, 25.29, 15.42, 12.34, 30.45],
}

sns.barplot(data=data, x="total_bill", y="day", color="blue")
plt.show()