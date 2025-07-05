import time, sys

indent =  0
direction = True

while True:
    print(" "*indent, end="")
    print("****")
    time.sleep(0.05)
    if direction:
        indent+=1
        if indent ==10:
            direction = False
    else:
        indent-=1
        if indent == 0:
            direction = True    
    