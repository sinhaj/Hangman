# Python Program to illustrate
# Hangman Game
import random
from collections import Counter

bollyWood = '''tubelight,mom,raees,race, 
               kaabil,newton,simran,noor 
               ittefaq,phillauri,poorna 
               chef,raabta,fukrey,kaalakandi, kal ho na ho, fukrey returns'''

bollyWood = bollyWood.split(',')

movie = random.choice(bollyWood)

if __name__ == '__main__':
    print('Guess the movie!')

    for i in movie:

        print('_', end=' ')
    print()

    playing = True

    letterGuessed = ''
    chances = len(movie) + 2
    correct = 0

    try:
        while (chances != 0):
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue

            # Validation of the guess
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue

            # If letter is guessed correcly
            if guess in movie:
                letterGuessed += guess

            # Print the word
            for char in movie:
                if char in letterGuessed:
                    print(char, end=' ')
                    correct += 1
                else:
                    print('_', end=' ')

                # If user has guessed all the letters
            if (Counter(letterGuessed) == Counter(movie)):
                print()
                print('Congratulations, You won!')
                break


        if chances == 0:
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(movie))

    except KeyboardInterrupt:
        print()
        print('Oops! Try again.')
        exit()




