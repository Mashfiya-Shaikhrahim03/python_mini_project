import random
try :
 top_of_range = int(input("Type a number : "))
#  print(top_of_range)
except :
 print("please enter valid number!")

if top_of_range <= 0 :
   print("please type a number larger/greater than 0 next time.") 
   quit()

random_number = random.randint(0 , top_of_range)
guessess = 0

while True :
  guessess += 1
  try :
    user_guess = int(input("make a guess "))
  except :
    print("Invalid number, please try again!")
    continue
  
  if user_guess == random_number:
    print(f"You win! The number was {random_number}")
    print(f"You guessed it in {guessess} guesses!")
    break
  elif user_guess > random_number:
    print("you were above the number!")
  else:
     print("you were below the number!")