from hangman_words import word_list
from hangman_art import logo,stages

import random

print(logo)

word = random.choice(word_list)

print(word)

ans = []

for i in word:
    ans.append("_ ")


# print(' '.join(ans))


print("\n")


lives = 7

while lives>0 and ans.count("_ ") != 0:
    guess = input("Guess a letter:").lower()
    a = 0
    for i in range(0, len(word)):
        if word[i] == guess and ans[i] == "_ ":
            ans[i] = guess
            a = 1
    if a == 0:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives = lives-1

    else:
        a = 0
    print(stages[lives - 1])
    print(f"Number of lives left: {lives}")


    print(' '.join(ans))
if lives>=0 and ans.count("_ ")==0:
    print(f"Congratulations!! You Guessed the right word: {word}")
else:
    print("You losses all your lives :-(...better luck next time!!")