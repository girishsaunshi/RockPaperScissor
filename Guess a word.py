import random

def pick_word():
    # List of words for the game
    words = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'watermelon', 'strawberry', 'blueberry']
    return random.choice(words)

def display_word(word, guessed_letters):
    # Display the word with guessed letters and underscores for unguessed letters
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display

def guess_word():
    secret_word = pick_word()
    guessed = []
    attempts = len(secret_word) + 2
    print("Welcome to the Word Guessing Game!")
    print(display_word(secret_word, guessed))

    while attempts > 0:
        print(f"You have {attempts} attempts left.")
        guess = input("Guess a letter or the whole word: ").lower()

        if len(guess) == 1:  # Guessing a single letter
            if guess in guessed:
                print("You've already guessed that letter.")
            elif guess in secret_word:
                print("Good guess!")
                guessed.append(guess)
                print(display_word(secret_word, guessed))
            else:
                print("Wrong guess!")
                attempts -= 1
                print(display_word(secret_word, guessed))
        else:  # Guessing the whole word
            if guess == secret_word:
                print("Congratulations! You've guessed the word!")
            else:
                print("That's not the word!")
            break

        if '_' not in display_word(secret_word, guessed):
            print("Congratulations! You've guessed the word!")
            break

    if attempts == 0:
        print(f"Sorry, you're out of attempts. The word was '{secret_word}'.")

# Start the game
guess_word()
