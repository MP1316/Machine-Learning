# def sum(a,b):
#     c= a + b
#     print("The sum of", a, "and", b, "is:", c)


# sum(5, 10)  
# sum(20, 30)  

"""
def sum(a,b):
    c= a + b
    return c

result1 = sum(5, 10)
print("The sum of 5 and 10 is:", result1)
result2 = sum(20, 30)
print("The sum of 20 and 30 is:", result2)

"""

def marks(m1, m2, m3):
    total = m1 + m2 + m3
    percentage = (total / 300) * 100
    return total, percentage

total_marks, avg_percentage = marks(85, 90, 95)
print("Total marks:", total_marks)
print("Average percentage:", avg_percentage)