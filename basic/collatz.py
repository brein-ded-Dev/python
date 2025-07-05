

def collatz(number):
    print(int(number), end="  ")

    if number == 1:
        return number
    elif number %2 == 0:
        return collatz(number/2)
    else:
        return collatz(3*number+1)
    


print("Please enter a number")
number= input(">")
if(number.isnumeric()):
    number = int(number)
    collatz(number)
else:
    print("Please enter a valid number")