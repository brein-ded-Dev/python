import random

# b= ["H"] *6
# a= ["T"] *6

# times =0; 
# for l in range(1000):
#     test = [random.choice(["H", "T"]) for l in range(100)]     
    
#     for i in range(6,len(test)+1):
#         if test[i-6:i] == a or test[i-6:i] == b:
#             times+=1
        

# print(times)


b= ["H"] *6
a= ["T"] *6

times =0; 
test = [0] * 100
for l in range(1000):
    for i in range(len(test)):
        test[i] = random.choice(["H","T"])
        
        if i>5 and test[i-6:i] == a or test[i-6:i] == b: #if the first part of the and statement fails the code skips the entire statements and marks as false. 
             times+=1
            

print(times)