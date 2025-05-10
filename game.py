import random
import string
words = ["aback", "abaft", "abandoned", "abashed", "aberrant", "abhorrent", "abiding"]
def get_valid_word(word_list):
    word = random.choice(word_list)
    while '-' in word or ' ' in word:
        word = random.choice(word_list)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 6

    print("Welcome to Hangman!")

    while len(word_letters) > 0 and lives > 0:
        print(f"\nYou have {lives} lives left and used letters: {' '.join(sorted(used_letters))}")
        
        # Show current word status
        word_display = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_display))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print(f"Letter {user_letter} is not in the word.")
        elif user_letter in used_letters:
            print("You already used that letter. Try again.")
        else:
            print("Invalid character. Please enter a letter.")

    # Game over
    if lives == 0:
        print(f"\nYou died! The word was {word}")
    else:
        print(f"\nCongratulations! You guessed the word: {word}")

# Run the game
hangman()
