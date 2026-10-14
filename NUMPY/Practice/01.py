import numpy as np
# arr = np.array([10, 20, 30, 40])

# print("Shape :", np.shape(arr))
# print("Size :", np.size(arr))
# print("Dimension :", np.ndim(arr))
# print("Datatype :", arr.dtype)


"""
arr = np.arange(1,21)

for num in arr:
    if num %2 ==0:
        print(num, end=" ")
        
for i in range(1,21):
    if i %2 ==0:
        print(i, end=" ")

"""
# print(np.full((3,3), 0))

# arr = np.arange(1,13)
# print(np.reshape(arr, (3,4)))

# arr = np.array([5,10,15,20,25])
# print("Maximun", np.max(arr))
# print("Minimun", np.min(arr))
# print("Sum", np.sum(arr))
# print("Mean", np.mean(arr))

"""

# Indexing, Slicing and Modification

# arr = np.array([10, 20, 30, 40, 50, 60])
# print(arr[2:5])

# arr = np.array([1,2,3,4,5])
# print(arr*10)

# arr = np.array([10,20,30,40])
# print(np.insert(arr, 2, 99))

# arr = np.array([10,20,30,40])
# mask = arr>20
# print(mask)
# print(arr[mask])

# arr1 = [1,2,3]
# arr2 = [4,5,6]
# vertically_stack = np.vstack((arr1, arr2))
# print(vertically_stack)

# arr1 = [1,2,3]
# arr2 = [4,5,6]
# horizontally_stack = np.hstack((arr1, arr2))
# print(horizontally_stack)


"""


# Statistical Functions

# arr = np.array([12,15,18,20,25,30])
# print("Mean :", np.mean(arr))
# print("Median:", np.median(arr))
# print("Varience :", np.var(arr))
# print("Standard deviation :", np.std(arr))

# arr = np.array([10,20,30,40,50,60,70])
# print("25th Percentile :", np.percentile(arr, 25))
# print("50th Percentile :", np.percentile(arr, 50))
# print("75th Percentile :", np.percentile(arr, 75))

# arr = np.array([45, 89, 23, 99, 67, 89])
# print("Maximum value", np.max(arr))
# print("Maximum index :", np.argmax(arr))

# arr = np.array([10, np.nan, 30, np.nan,50])
# is_null = np.isnan(arr)
# print(is_null)

# mean = np.nanmean(arr)
# arr[np.isnan(arr)] = mean
# print("Updated array:", arr)

# arr = np.array([10,20,30,40,50])
# normalized = (arr-(np.min(arr))/(np.max(arr)-np.min(arr)))
# print(normalized)

# arr = np.array([[1,2,3,4],
#                 [3,4,5,6],
#                 [8,3,9,5],
#                 [0,1,2,6]])

# # Diagonal element
# print("Diagonal :", np.diag(arr))
# print("Opposite Diagonal :", np.fliplr(arr))


# A = np.array([[1,2],
#               [3,4]])

# B = np.array([[5,6],
#               [7,8]])

# print(A*B)


# arr1 = np.array([[1,2,3],
#                   [5,6,7],
#                   [7,8,9]])

# arr2 = np.array([10,20,30])

# print("Broadcasting :", arr1+arr2)



arr = np.array([65,80,45,90,75,88,60,95,72,85])
print("Average :", np.mean(arr))
print("Highest Marks :", np.max(arr))
print("Minimun Marks :", np.min(arr))
print("Student Scoring above 75 :", np.sum(arr>75))
print("Sorted Marks :", np.sort(arr))











