"""
Welcome to our restaurant management system! 
This program allows you to manage your 
restaurant's menu, take orders, 
and generate bills for customers.

"""
menu = {
    "Burger": 90,
    "Pizza": 89,
    "Pasta": 79,
    "Salad": 49,
    "Soda": 19 
}
# print(menu)
print("Welcome to our restaurant!") 
print("burger: 90\nPizza: 89\nPasta: 79\nSalad: 49\nSoda: 19")
order_total = 0

item1 = input("Enter the name of the item you want to order: ")
if item1 in menu:
    order_total += menu[item1]
    print(f"Your item: {order_total} has been added to your order") 

else:
    print(f"Order item {item1} is not available in the menu.")

another_item = input("Do you want to order another item? (yes/no): ")
if another_item == "yes":
    item2 = input("Enter the name of the second item you want to order: ")
    if item2 in menu:
        order_total += menu[item2]
        print(f"Your item: {order_total} has been added to your order") 
    else:
        print(f"Order item {item2} is not available in the menu.")
print(f"Your total bill is: {order_total}")