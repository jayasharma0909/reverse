import random

print("~~~~~~Welcome to RPS~~~~~~~~")
user_score = 0
comp_score = 0
ties = 0
while True:
    name = input("Enter your name here: ")
    print(""" 
    Wining Rules:
    1. Paper Vs Rock ---> Paper
    2. Rock Vs Scissors --> Rock 
    3. Scissors Vs Paper --> Scissors """)

    print("""Choices are:
    1. Rock 
    2. Paper
    3. Scissors  """)

    print()
    Choice  = int(input("enter your choice from 1-3: "))
    print(Choice)
    while Choice  > 3 or Choice < 1:
        Choice = int(input("Enter vaild Input"))

    if Choice == 1:
        user_Choice = "Rock"
    elif Choice == 2:
        user_Choice = "Paper"
    else:
        user_Choice = "Scissors"

    print ("The User's choice his ", user_Choice)
    print ("Now it is Computer's turn")

    Computer = random.randint(1,3)
    if Computer == 1:
        Comp_Choice = "Rock"
    elif Computer == 2:
        comp_choice = "paper"
    else:
        Comp_Choice = "Scissors"
    print ("The Computer's choice is",  Comp_Choice )

    if ((user_Choice == "Paper" and Comp_Choice == "Rock") or (user_Choice == "Rock" and Comp_Choice == "Paper")):
        print("Paper Wins")
        result = "Paper"

    elif ((user_Choice == "Scissors" and Comp_Choice == "Rock") or (user_Choice == "Rock" and Comp_Choice == "Scissors")):
        print("Scissors Wins")
        result = "Scissors"
    elif ((user_Choice == Comp_Choice)):
        print("Tie")
        result = "Tie"
    else:
        print("Rock Wins")
        result = "Rock"

    if result == "Tie":
        ties += 1
    elif result == user_Choice:
        print("User Wins")
        user_score += 1
    else:
        print("Computer Wins")
        comp_score += 1 
    print("Scores are")
    print (name, "'s score is", user_score)
    print ("Computer's score is", comp_score)
    print ("ties are" , ties)
    repeat  = input("do you want to play again? ")
    if repeat == "No" or repeat == "No":
        "break"
        print("Game over!")
        print('thanks for playing !!!')