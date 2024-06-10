import random
import json
import sys

# Hangman figures
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\\  |
 / \\  |
     ===''']

def load_words_from_file(file):
#Loads the list of words from a JSON file
    with open(file, 'r') as file:
        #parse json file into python dict
        data = json.load(file)
    return data["words"]

def get_random_word(word_list):
    """Selects a random word from the word list."""
    random_word = (random.choice(word_list))
    len_random = len(random_word)
    print(f"The word contain {len_random} letters")
    return random_word
#display the current state of hangman.
def display_board(missed_letters, correct_letters, secret_word):
    #prints the hangman pic curresponding to the missed letters
   
    print(HANGMAN_PICS[len(missed_letters)])
    print()
    #print the missed letters user entered
    print("Missed letters:", end=" ")
    for letter in missed_letters:
        print(letter, end=" ")
    print("\n")
    #print the unguessed letters
    blanks = "_" * len(secret_word)

    for i in range(len(secret_word)):  # Replace blanks with correctly guessed letters
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
    chance = 7
    no_of_missed_letters = len(missed_letters)
    # no_of_correct_letters = len(correct_letters)
    no_of_chance_remaining = chance - no_of_missed_letters
   
    print(f"No of chance remaining = {no_of_chance_remaining}")
    letters_to_be_find = blanks.count('_')
    print(f"you have to uncover {letters_to_be_find} more letters")
    for letter in blanks:  # Show the secret word with spaces in between each letter
        print(letter, end=" ")
    print("\n")

def get_guess(already_guessed):
#Returns the letter the player entered. 
  
    while True:
       
        
        print("Guess a letter.")
        guess = input().lower()
        if len(guess) != 1:
            print("Please enter one letter at a time.")
        elif guess in already_guessed:
            print("You have already guessed. Choose another letter.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter a LETTER.")
        else:
              
            return guess
       
def play_again():
    """Returns True if the player wants to play again, otherwise it returns False."""
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith('y')

def main():
    #unpacking argv
    script,file = sys.argv

    print("H A N G M A N")
    missed_letters = ''
    correct_letters = ''
    words = load_words_from_file(file)
    secret_word = get_random_word(words)
    game_is_done = False

    while True:
        display_board(missed_letters, correct_letters, secret_word)

        # Let the player enter a letter.
        guess = get_guess(missed_letters + correct_letters)
       

        if guess in secret_word:
            correct_letters = correct_letters + guess

            # Check if the player has won
            found_all_letters = True
            for i in range(len(secret_word)):
                if secret_word[i] not in correct_letters:
                    found_all_letters = False
                    break
            if found_all_letters:
                print(f"Yes! The secret word is \"{secret_word}\"! You have won!")
                game_is_done = True
        else:
            missed_letters = missed_letters + guess

            # Check if player has guessed too many times and lost
            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                display_board(missed_letters, correct_letters, secret_word)
                print(f"You have run out of guesses!\nAfter {str(len(missed_letters))} missed guesses and {str(len(correct_letters))} correct guesses, the word was \"{secret_word}\".")
                game_is_done = True

        # Ask the player if they want to play again (but only if the game is done).
        if game_is_done:
            if play_again():
                missed_letters = ''
                correct_letters = ''
                game_is_done = False
                secret_word = get_random_word(words)
            else:
                break

if __name__ == "__main__":
    main()
