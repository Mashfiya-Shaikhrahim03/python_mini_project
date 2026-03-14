print("Welcome to my computer quiz!")
playing = input("Do you wanna play it? ")

if playing.lower() !=  "yes" :
    quit()
         
print("ohk! Let's play :) ") 
score = 0

answere = input("what does cpu stand for? ")
if answere.lower() == "central processing unit" :
    print("correct!")
    score += 1
else :
    print("Incorrect!!")    

answere = input("what does RAM stand for? ")
if answere.lower() == "random access memory" :
    print("correct!")
    score += 1
else :
    print("Incorrect!")    

answere = input("what does GPU stand for? ")
if answere.lower() == "graphics processing unit" :
    print("Correct!")
    score += 1
else :    
    print("Incorrect!")

answere = input("what does PSU stand for? ")
if answere.lower() == "power supply" :
    print("Correct!")
    score += 1
else :
    print("Incorrect!")    

print(f"You got {score} question correct!") 
print("you got " + str((score / 4) * 100) + "% .")   