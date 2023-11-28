import random
import sys
import os
chambers = input("Enter the number of chambers (default = 6):")
terminator = 0

if not chambers:
    chambers = 5
elif (not(chambers.isdigit()) or (int(chambers) >6 ) or (int(chambers) < 0)) :
    print("Invalid Chamber input")
    terminator = 1
    #os.execv(sys.executable, [sys.executable] + sys.argv)
while ( terminator == 0): 
    bullet = random.randint(1,int(chambers))
    for i in range(1, int(chambers)+1):
        input("Press enter to pull the trigger:")
        if (i == bullet):
            print("You just got served!")
            #payload
            terminator =1
            break
        else:
            print("You will live to see another day!")
