master_pwd = input("What is the master password? : ")

def view() :
    with open("password.txt" , "r") as f :
     for lines in f.readlines() :
        print(lines.rstrip())
    

def add() :
    name = input("Enter account name: ")
    pwd = input("Enter password: ")

    with open("password.txt" , "a") as f :
        f.write("Account_name: " + name + "|" + "Password: " + pwd + "\n")
    
     
while True :
    mode = input("Would you like to add new password or view exsisting ones (view / add), press Q to quit: ")

    if mode == "q" :
        break
    if mode == "view" :
        view()
    elif mode == "add" :
        add()
    else :
        print("Invalid mode")
        continue