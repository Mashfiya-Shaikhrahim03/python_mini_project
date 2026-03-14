print("Welcome to our restaurant, Here is the menu :\n")

# define the menu of resturant
menu = {
    "pizza" : 150 ,
    "cold coffe" : 60 ,
    "noodels" : 50 , 
    "ice-cream" : 30 ,
}

# Greetings
# print("Welcome to salashy RESTAURAN :")
# print("pizza : 150\ncold coffe : 60\nnudals : 50\nice-cream : 30")
# Display menu properly
for item, price in menu.items():
    print(f"{item} = {price}")

order_total = 0

# first order
item_1 = input("\nEnter the name of items you want to order :").lower()

if item_1 in menu :
    order_total = order_total + menu[item_1] # 0 + 30 => 30
    print(f"your item {item_1} has been added to your oder")
else:
    print(f"odered item {item_1} is not available yet.")   


# second order
another_order = input("\nDo you want to add another item ? (yes / no)\n").lower()   

if another_order == "yes":
    item_2 = input("Enter the name of second order item : ").lower()
    if  item_2 in menu :
        order_total += menu[item_2]
        print(f"item {item_2} has been added to order")
    else :
       print(f"ordered item {item_2} is not available!")        

print(f"\nThe total amount of your odered to pay : {order_total}")    