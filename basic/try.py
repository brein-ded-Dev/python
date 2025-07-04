
print("Hello, World!")
print("What is your name?")
name =input ('Name: ' ) #all inputs are string, numbers require explicit conversion

print("Hello, " + name + "!")
print(len(name))
print(type(name)) #type() function is used to check the type of a variable

#opposite day

today_is_opposite_day = True
if today_is_opposite_day:
    today_is_opposite_day= True
else:
    today_is_opposite_day = False
    
if today_is_opposite_day:
    today_is_opposite_day = not today_is_opposite_day

if today_is_opposite_day:
    print("Today is opposite day!")
else:
    print("Today is not opposite day!")
