import random

name=input("What is your name? ")
print("Good luck!",name)

print("Guess the characters")
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'himanshi']
target=random.choice(words)
guesses=" "
turns=12
while turns>0:
    failed=0
    for char in target:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed+=1

    if failed==0:
        print("\n You win")   
        print("The word is :",target)
        break
    print()
    guess=input("Guess the character: ")
    guesses+=guess
    if guess not in target:
        turns-=1
        print("wrong")
        print("you have ",+turns," more guesses")
        if turns==0:
            print("You loose")




