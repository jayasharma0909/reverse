import random
print("~~~~~~~Welcome to Dice game~~~~~~~")
min = 1
max = 6
while True:
    name = input("Enter your name here :")
    print("1. roll the dice 2. exit ")
    user = int(input(" What is your choice from the above? enter number: "  ))
    if user==1:
        number = random.randint(1,6)
        print(number)
    else:
        break


