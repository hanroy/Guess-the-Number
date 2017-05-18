from random import *

answer = raw_input("Do you wanna play [Y/N] : ")
guessnumber = randint(1, 15)

while (answer == "Y"):
    userguess = int(raw_input("Guess a number: ")) 
    if userguess < guessnumber:
        print ("Little Higher")
    elif userguess > guessnumber:
        print ("Little Lower")
    else: 
        print "Well done"
        break
else :
   print("Bye!.")

