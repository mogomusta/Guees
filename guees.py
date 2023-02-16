def hangman_init():
    print("Welcome to Hangman!")


def get_user_input(prompt):
    input = raw_input(prompt)
    return input

# return list of char indexes in str


def find_substr_in_str(string, test_char):
    return [pos for pos, char in enumerate(string) if char == test_char]


def guess_letter(word):
    guessing = True
    letter_guessed = []
    start_word = len(word) * ['_']
    number_incorrect_guesses = 0

    while (guessing):
        print(' '.join(start_word))
        if ('_' not in start_word):
            print("Congratulations you have correctly guessed: " + word.upper())
            guessing = False
            break

        user_letter = get_user_input("Guess your letter:")
        user_letter = user_letter.upper()

        if (user_letter in letter_guessed):
            print("You have already guessed this letter!")
            number_incorrect_guesses += 1
        # it is much quicker to search a set instead of a list for large data size
        elif (user_letter in set(word)):
            print("Correct")
            char_location = find_substr_in_str(word, user_letter)
            for idx in char_location:
                start_word[idx] = user_letter
        else:
            print("Incorrect")
            number_incorrect_guesses += 1

        letter_guessed.append(user_letter)
        if (number_incorrect_guesses == 6):
            print("You have made 6 incorrect guesses, you lose!")
            guessing = False


def main():
    test_word = "EVAPORATE"
    hangman_init()
    guess_letter(test_word)


if __name__ == '__main__':
    main()
