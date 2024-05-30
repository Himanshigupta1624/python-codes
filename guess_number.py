# import random

# target=random.randint(1,100)


# while True:
#     userChoice=int(input("Enter the number or Quit(Q) :"))
#     if(userChoice=="Quit"):
#         break
#     userChoice=int(userChoice)
#     if(userChoice==target):
#         print("Success : Correct Guess!!")
#         break
#     elif(userChoice<target):
#         print("Your number was too small. Take a bigger guess...!!")
#     else:
#          print("Your number was too big. Take a smaller guess...!!")  



# print("---------Game over-------")

import random
import math
Q=""
lower=int(input("Enter the lower bound :- "))
upper=int(input("Enter the upper bound :- "))

target=random.randint(lower,upper)
print("\n You have only",round(math.log(upper-lower +1,2)),"chnaces to guess an integer")
count=0
while count<math.log(upper-lower +1,2):
    count+=1

    userchoice=int(input("Enter the number or Quit(Q):- "))
    if(userchoice==Q):
        break
    elif(userchoice==target):
        print("congratulations you did it in ",count,"try")
        break
    elif(userchoice<target):
        print("Your number is too small !!")
    elif(userchoice>target):
        print("Your number is too big !!")

if count>math.log(upper-lower+1,2):
    print("the number is ",target)
    print("Better luck next time")            