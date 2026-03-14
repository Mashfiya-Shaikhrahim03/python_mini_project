name = input("Type your name : ")
print("Welcome to jumanji adventure Game!" , name)

print("Here are some ways to playing this game like choose(left/right) ways and find your treasure & if you want to quit then type Q: ")

user_enter = input("Enter your choice : ")
if user_enter.lower() == "q" :
    quit()
user_score = 0
if user_enter.lower() == "left" :
    print("Welcome to jumanji jungle and solve puzzles!")

    print("a = 120 & b = 23 , a + b ?  ")
    user_answere = input("Tell your answere : ")

    if user_answere == "143" :
        print("Good catch! , go ahead!")
    else :
        print("you lost!")
        quit()

    print("a = 34 & b = 23 , a - b ?  ") 
    user_answere = input("Tell your answere : ")
    
    if user_answere == "11" :
        print("Good catch! , go ahead!")

    else :
        print("you lost!")
        quit() 
    print("youre last puzzle then you find youre treasure")
    print("if I have 87 apples then I throgh away 30 apples and add some orange then , How many apples I have?")      

    user_answere = input("Tell the answere: ")
    if user_answere == "57" :
        print("Amazing! youre very near to win.")
    else :
        print("you lost")
        quit()  
    
        print("Now you reached finals to achieve your goal!")
        print("if a number is multiplied by 0, what will the answer always be? ")

    user_answere = input("Tell me answer: ")

    if user_answere == ["zero" , 0] :
        print("Congress!!!, you Winn...")
    else :
        print("you trying hard but you Lost!!")
    quit()


if user_enter.lower() == "right" :
    print("Good choice! go ahead and find your treasure.") 
    print("But here is some common based question to win you!!")
    

    print("If you brush your teeth 2 times a day, how many times will you brush in 7 days? ")
    user_answere = input("Type your answer: ")

    if user_answere == "14" :
        print("Go catch! solve next one...")
        user_score += 1
    else :
        print("youre lost but you have an advantage!")

    print("If school started at 8 AM and ends at 2 PM, how many hours is the school time? ")
    user_answere = input("Type here your answer: ")
    if user_answere == "6" :
         print("Go catch! solve next one...")
         user_score += 1
    else :
        print("youre lost but you have an advantage!")


    print("A boy has 3 apples. He eats 1 and gives 1 to his frined. How many apples are left? ")
    user_answere = input("Type youre answer: ")
    if user_answere == "1" :
         print("Go catch! solve next one...")
         user_score += 1
    else :
        print("youre lost but you have an advantage!")

    print("Now last one...")
    print("A rooster lays one egg every day. How many eggs will it lay in 10 days? ")
    user_answere = input("Type your answer: ")

    if user_answere == "zero" or user_answere == "0" :
         print("Wonderfulll.... You naild it!!")
         user_score += 1
    else :
        print("Appreciate it but you lost the game!!")
        quit()

    print(f"you're total score {user_score}")

else :
   print("Invalid option!")    