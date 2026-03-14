import random

user_score = 0
comp_score = 0
options = ["rock", "paper" , "scissors"]

while True :
    user_input = input("Type rock/paper/scissor or Q to quit: ").lower()
    if user_input == "q" :
        break
    if user_input not in options :
        continue

    random_num = random.randint(0 , 2)
    # rock = 0 , paper = 1 , scissor = 2

    comp_pick = options[random_num]
    print("computer_picked" , comp_pick + ".")

    if user_input == "rock" and comp_pick == "scissors" :
        print("you won!")
        user_score += 1

    elif user_input == "paper" and comp_pick == "rock" :
        print("you won!")
        user_score += 1

    elif user_input == "scisoors" and comp_pick == "paper" :
         print("you won!")
         user_score += 1

    else :
        print("You lost!")
        comp_score += 1

print(f"you won! {user_score} times.")
print(f"The computer won! {comp_score} times.")
print("The End...")