"""
Q1->Print this pattern
****
****
****
****

"""

# for i in range(4):
#     for j in range(4):
#         print("*", end=" ")
#     print()

"""
Q2->Print this pattern
*
**
***
****

"""

# for i in range(1, 4+1):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()

"""
Q3->Print this pattern
****
***
**
*
"""

# for i in range(4, 0, -1):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()     

"""
Q4->Print this pattern
1
12
123
1234

"""

for i in range(1, 4+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()



