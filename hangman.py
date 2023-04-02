from logolar import logo
from logolar import stages
from words import word_list
import random


print(logo)




chosen_word = random.choice(word_list)
letter_count = len(chosen_word)
lives =6
words= []

for _ in chosen_word:
    words += "_"
    
print(words)
print(f"psst the word is:{chosen_word}")
print(stages[lives])

game_= True

while game_:
    guess_letter = str(input("Please guess a word!"))
    for position in range(letter_count):
            letter = chosen_word[position]#calis
            if letter == guess_letter:
                  words[position]= letter
    if guess_letter not in chosen_word:
        lives= lives -1
        print(stages[lives]) # 6-5-4-3-2-1-0
    
    print(f"{' '.join(words)}")
    if "_" not in words:
        print("You winnnnnnnnnnnn!")
        game_= False

    if lives == 0:
        print("lo0o0o0o0o0o0o0oo00se!!!!!!!!!")
        game_ = False