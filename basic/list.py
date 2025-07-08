
import random 
data = ["This", "is", "the", "List","data","type","in","python"],["comparable","to","array","but","better."]
print(data)

print(data[0]) # the 0th list.
print(data[1]) # the 1st list 
print(data[1][0]) # The 0th element of the 1st list.
print(data[0][4]) # the 4th element of the 0th list
print(data[-1]) # the last index of the list
print(data[0][-8]) #the 8th spot from backwards of the 0th list
print(data[0][3:7]) #data from the 0th list of 3rd - 7th element (3rd included 7 excluded)
print(len(data)) #elements in the data varaible
print(len(data[0])) # elements in the 0th list fo the data variable. 

data = data[0]+data[1] #concatenation 
print(len(data))
data = data*2 #replication
print(data)

del data[2] #del is a keyword to delete an element
print(data[2])

for i in range(len(data)): #for loop across the data list.
    print("",end="")
    
print('This'in data) #checking if provided element is present in the list
print('this'in data)
print('This'not in data)
print('this'not in data) 

multiple = ["Used","for","multiple","assignment"]
variable, number, must, same = multiple

for index, element in enumerate(multiple):
    print("Index "+str(index)+" and elements "+ element) #the enummerate funciton can be used to find out the index and the respective element on that index

print(random.choice(data)) #chooses a random element from the list
random.shuffle(multiple) #shuffles the list.
print(multiple)
print(multiple.index("Used")) #inbuilt funciton that returns the value of the index if the element is found, value error if not.

#functions to insert elements
multiple.append("elements")
multiple.insert(-1,"adding")

print(multiple)

#function  to remove element
multiple.remove("for")

#sorting lists in alphabetical order
multiple.sort()
multiple.sort(reverse=True)
multiple.reverse() #reverses the list in place

print(multiple)