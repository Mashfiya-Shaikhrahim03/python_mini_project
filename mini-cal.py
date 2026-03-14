print("WELCOM TO MY mini-calculator =>")
num1 = int(input("Enter 1st number :"))

num2 = int(input("Enter 2nd number :"))
operation = input("Enter choice operator : ")
if operation == "+" :
    print("Adding numbers : " , num1 + num2)
elif operation == "-" :
    print("substracting number : " , num1 - num2)
elif operation == "*" :
    print("multiplying numbers :" , num1 * num2)
elif operation == "/" :
    print("divinding numbrs : " , num1 / num2)
elif operation == "%" :
    print("reminder of two numbers :" , num1 % num2) 
elif operation == "**" :
    print("power of two numbers : ", num1**num2) 
else :
    print("something went wrong... try again!")              