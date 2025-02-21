import random
lives=6
list_of_words=["python","hangman","game","computer"]
word=random.choice(list_of_words)
print("chosen wors is:",word)
display=[]
for i in range(len(word)):
    display.append("_")
print(display)
j=False
while not j:
    guessed_letter=input("Guess a letter: ").lower()
    for position in range(len(word)):
        letter=word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)
    if guessed_letter not in word:
        lives-=1
        print("Your remaining lives is",lives)
        if lives==0:
            j=True
            print("You loose!!")
    if '_' not in display:
        j=True
        print("You win!!")
    
            
            
