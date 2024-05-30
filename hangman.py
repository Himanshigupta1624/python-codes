import random
# somewords=["apple" ,"banana", "mango","strawberry",  
# "orange", "grape" "pineapple "," watermelon" 
# ,"peach"," muskmelon"]
f=open("somewords.txt","r")
data=f.readline()
somewords=data.split()
word=random.choice(somewords)
total_chance=7
print("Guess the word! HINT: word is a name of fruit")
guessed_word="-" *len(word)

while total_chance !=0:
   print(guessed_word)
   letter=input("Guess a letter ")
   if letter in word:
        for index in range(len(word)):
            if word[index]==letter:
                guessed_word=guessed_word[ :index]+letter+guessed_word[index+1:]
                
        if guessed_word==word:
            print("Congratulations you won !!")      
            break
   else:
       total_chance -=1
       print("Incorrect guess")
       print("the remaining chances are :",total_chance)
else:
    print("Gamne over")
    print("All the chances are exhausted")    
    print("You lose") 
print("The word is",word)  