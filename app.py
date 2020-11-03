from words import game_words
import random


def start_game():
    # Select a word from the list of words.
    selected_word = game_words[random.randint(0, len(game_words) - 1)]
    print('The word is an ' + str(len(selected_word)) + ' letter word.')
    correctly_guessed_letters = []
    word_placeholder = display_word_placeholder(
        selected_word, correctly_guessed_letters)

    # User has 10 attempts at guessing.
    attemptsLeft = 10
    while attemptsLeft >= 1 and ('__' in word_placeholder):
        print(word_placeholder)
        user_input = input('Guess a letter. \n')
        if len(user_input) > 1:
            print('Please only type one letter.')
        elif user_input in selected_word:
            print('Well done. \'' + user_input + '\' is in the word.')
            correctly_guessed_letters.append(user_input)
        elif user_input not in selected_word:
            print('Sorry. \'' + user_input + '\' is not in the word.')
            attemptsLeft -= 1
            print(str(attemptsLeft) + '/10 attempts left.')
        word_placeholder = display_word_placeholder(
            selected_word, correctly_guessed_letters)

    if attemptsLeft == 0 and '__' in word_placeholder:
        print('Hangman! Game over! You were unable to guess the word: ' + selected_word)
    else:
        print('Well done! You guessed the word: ' + selected_word)


# Returns the guessed letters against non-guessed letters e.g '__ x a __ __ e'
def display_word_placeholder(word, correctly_guessed_letters):
    word_placeholder = ''
    for char in word:
        if char in correctly_guessed_letters:
            word_placeholder += char + ' '
        else:
            word_placeholder += '__ '

    return word_placeholder


start_game()
