import random
from hangmanword import word_list

word = word_list
picked = random.choice(word)
right = ['_'] * len(picked)
wrong = []
lives = 8
x = len(picked) - 1


def update():
    for i in right:
        print(i, end=' ')
    print()


while lives > 0:
    guess = input('Guess a letter: ')
    if guess in picked:
        index = 0
        for i in picked:
            if i == guess:
                right[index] = guess
            index = index + 1
        update()
        x -= 1
        if x < 0:
            break

    else:
        if guess not in wrong:
            wrong.append(guess)
            print(wrong)
            update()
            lives -= 1
        else:
            print('You already guessed it')

if lives == 0:
    print('You lost')
else:
    print('You win')
