"""
n = int(input("Enter start number: "))
m = int(input("Enter end number: "))
for i in range(n, m-1, -1):
    print(n)
    n-=1
    
    """
num = int(input("Enter a number : "))
n = int(input("Enter start number: "))
m = int(input("Enter end number: "))
for i in range(n, m):
    if i % num == 0:
        print(i)
        