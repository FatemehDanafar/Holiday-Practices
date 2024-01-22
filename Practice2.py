import random
userM = 0
comM = 0
Option=["Rock","Paper","Scissor"]

for i in range(5):
    print(" Rock  Paper  Scissor")
    user = input("Enter Your Choise: ")
    computer = random.choice(Option)

    if user == computer:
        print("Both Choises are the same!")
    elif user == "Rock" and computer == "Paper":
        print("Sorry! you lose.")
        comM +=1
    elif user == "Rock" and computer == "Scissor":
        print("you Win!")
        userM +=1
    elif user == "Paper" and computer == "Rock":
        print("you Win!")
        userM +=1
    elif user == "Paper" and computer == "Scissor":
        print("Sorry! you lose.")
        comM +=1
    elif user == "Scissor" and computer == "Rock":
        print("Sorry! you lose.")
        comM +=1
    elif user == "Scissor" and computer == "Paper":
        print("you Win!")
        user +=1

print("your Mark" ,userM)
print("Computer Mark" ,comM)
    
    
