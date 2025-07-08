import sys, random, time

wid = 70
col = [0] *wid

while True: #downward traversal
    for i in range(wid): #horizontal traversal
        if random.random()<0.02:
            col[i] = random.randint(4,14) #defines how long a singular line be
        
        if col[i] ==0: #ignore unchanged numbers of the list
            print(" ", end=" ")
        else:
            print(random.choice([0,1]), end=" ") #print  if a value other than 0 exist. 
            col[i]-=1 #this is why above we have 4-14
    print()
    time.sleep(0.1)