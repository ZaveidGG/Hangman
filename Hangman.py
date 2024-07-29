import random
import hangman_words as hmwords
import hangman_art as hmart
import os

print(hmart.logo)

gameOver = False
display = []
strDisplay = ""
life = 6

chosenWord = random.choice(hmwords.word_list)

for letter in chosenWord:
    display.append('_')

while not gameOver:
    guessLetter = input("Guess a letter: \n").lower()

    for i in range(len(chosenWord)):
        letter = chosenWord[i]

        if letter == guessLetter:
            display[i] = letter

    print(f"{' '.join(display)}")

    if guessLetter in chosenWord:
        print(f"You have guessed a correct letter: {guessLetter}")
    elif guessLetter not in chosenWord:
        life-=1
        print(f"That's an incorrect letter. You lost a life")
        print(hmart.stages[life])
        if life==0:
            gameOver = True
            print("Game Over!")

    if "_" not in display:
        gameOver = True
        print("You have won")
