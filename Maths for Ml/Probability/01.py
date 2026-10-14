import numpy as np
import math
import random

"""
count_head = 0
for i in range(100):
    if random.choice(["Head", "tail"]) == "Head":
        count_head += 1
print(count_head)

"""

# result = np.random.randint(1,6)
# print(result)

# result = np.random.uniform(0,2)
# print(result)

count_head = 0
count_tail = 0
for i in range(100):
    result = random.choice(["Head", "Tail"])
    if result == "Head":
        count_head += 1
    else:
        
        count_tail += 1
print("Head Count", count_head)
print("Tail Count", count_tail)
