string = "My name is 'mohit'"
# print(len(string))
# print(string[0:-2])

"""
l = len(string)
i = 0

while i<l :
    print(string[i], end=" ")
    i=i+1


i = 1
l = len(string)
# i = 1
while i<=l:
   print(string[-i], end=" ")
   i +=1
   
   """

# new_string = string.replace("mohit", "Mohit")
# print(new_string)


# for i in string[::-1]:
#     print(i, end=" ")

"""

# Remove extra spaces from string
# lstrip use to remove left side spaces
# rstrip use to remove right side spaces
# strip use to remove both side spaces
string = "   My name is mohit  "
string = string.strip()
print(string)

"""


# count specific character in string
total = string.count("i")
print("Total occurrences of 'i':", total)