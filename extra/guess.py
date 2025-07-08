from random import*

number = randint(1,20)
guess = ""

print("Enter your guess:")
while True:
    guess = input('<')
    if not guess.isdigit():
        print("Enter a valid Number")
        continue
    if (int(guess)>number):
        print("Too high, Try again.")
        continue
    elif (int(guess)<number):
        print("Too low, Try again.")
        continue
    elif (int(guess)==number):
        print("Jackpot, You've won nothing.")
        break

    