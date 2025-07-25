
number = int(input("->"))
print(f"There is a better way to print shit {number}")
print('We simply need to use the "f" prefix before using the quotes, then we can directly use variables inside{}')
number *= int(input("->"))
print(f"Input function can have direct conversion and rather easier format of direct calculations as well{number}")

times_a_week = int(input("How many times a week do you eat at the student cafeteria?"))
price = float(input("The price of a typical student lunch?"))
groceries = float(input("How much money do you spend on groceries in a week?"))

print("Average food expenditure:")
print(f"Daily: {1.5+(groceries//7)} euros" )
print(f"Weekly: {groceries+price*times_a_week} euros")

if int(input("Shockingly valid syntax")) == 1984:
    print("Orwell")
    
    
int(input(""))
print(f"")
input("")
if __name__ == "__main__":
    print