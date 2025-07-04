import random

name = "exit"
while True:
    print("Please type your name:")
  #  name = input('>')
    if name == "exit":
        print("Goodbye!")
        break
    elif name == "hello":
        print("Hello, World!")
    else:
        print("Hello, {name}!")
        print("Please try again.")

print("Seems like you made it")

#name = ''
print(name)
while  not name :
    print("Enter name again")
   # name= input(">") 
    
    
for i in range(5):
    print(str(i))
    
print(flush=None)

for i in range(8,14):
    print(str(i))

print(flush=None)

for i in range(14,8,-1):
    print(str(i))

print(flush=None)

for i in range(5):
    print(random.randint(1,100))
