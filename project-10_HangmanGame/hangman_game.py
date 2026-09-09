import random
import hangman_stages
import fruits

lives=6
choosen_word=random.choice(fruits.word_list)

display=[]

for i in range(len(choosen_word)):
    display.append("_")
print(display)

game_over=False

while not game_over:
    guessed_letter=input("Guess the letter: ").lower()
    for position in range(len(choosen_word)):
        if choosen_word[position]==guessed_letter: 
            display[position]=guessed_letter
    print(display)
    if guessed_letter not in choosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("You Lose.")
    if "_" not in display:
        game_over=True
        print("You Win!!")  
    print(hangman_stages.stages[lives-1])
