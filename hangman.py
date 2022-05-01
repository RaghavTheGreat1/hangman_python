import os
import hangman_art
import random_word

get_random_word = random_word.RandomWords().get_random_word()

splitted_random_word = list(get_random_word.lower())


def generate_dashed_list(splitted_word):
    return ["_" for word in splitted_word]


initial_word_setup = generate_dashed_list(splitted_word=splitted_random_word)

death_countdown = len(hangman_art.stages)

didWon = False

print(hangman_art.logo)

while death_countdown > 0:
    if(splitted_random_word == initial_word_setup):
        didWon = True
        break
    guess_letter = input('Enter letter to guess: ').lower()
    os.system('CLS')
    flag_splitted_word = initial_word_setup.copy()

    for i in range(0, len(get_random_word), 1):
        if(splitted_random_word[i] == guess_letter):
            initial_word_setup[i] = guess_letter
            

    if(flag_splitted_word == initial_word_setup):
        print(f'You guessed {guess_letter} which is incorrect and hence you lose a life')
        death_countdown = death_countdown - 1
        print(hangman_art.stages[death_countdown])

    print(''.join(initial_word_setup))

if(didWon):
    print('Congratulations!! You managed to save a guy from being hanged')
else: 
    print(f'And there he was penalized... The correct word was {get_random_word}')