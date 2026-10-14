mylist = []
input_list = int(input("Enter the list element:"))
mylist.append(input_list)
print("Mylist:", mylist)

target_element = int(input("Enter target element:"))
for i in range(len(mylist)):
        if mylist[i] == target_element:
            print("Target element found at index:", i)
            break
else:
    print("Element not found:")


