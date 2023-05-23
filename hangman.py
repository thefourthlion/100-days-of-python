import random

# List of words for the game
word_list = ["hangman", "python", "computer", "programming", "openai", "game"]

# ASCII art for the hangman stages
hangman_stages = [
    """
       ________
      |        |
      |        O
      |       \\|/
      |        |
      |       / \\
     _|_
    """,
    """
       ________
      |        |
      |        O
      |       \\|/
      |        |
      |       /
     _|_
    """,
    """
       ________
      |        |
      |        O
      |       \\|/
      |        |
      |
     _|_
    """,
    """
       ________
      |        |
      |        O
      |       \\|
      |        |
      |
     _|_
    """,
    """
       ________
      |        |
      |        O
      |        |
      |        |
      |
     _|_
    """,
    """
       ________
      |        |
      |        O
      |
      |
      |
     _|_
    """,
    """
       ________
      |        |
      |
      |
      |
      |
     _|_
    """
]

def select_word():
    """Selects a random word from the word list."""
    return random.choice(word_list)

def display_word(word, guesses):
    """Displays the word with underscores for unguessed letters."""
    displayed_word = ""
    for letter in word:
        if letter in guesses:
            displayed_word += letter
        else:
            displayed_word += "_"
        displayed_word += " "
    return displayed_word

def play_game():
    """Main function to play the hangman game."""
    print("Welcome to Hangman!")
    word = select_word()
    guesses = []
    attempts = len(hangman_stages) - 1
    game_over = False
    
    while not game_over:
        print(hangman_stages[attempts])
        print(display_word(word, guesses))
        guess = input("Guess a letter: ").lower()
        
        if guess.isalpha() and len(guess) == 1:
            if guess in guesses:
                print("You already guessed that letter!")
            else:
                guesses.append(guess)
                if guess not in word:
                    attempts -= 1
                    print("Incorrect guess!")
                    if attempts == 0:
                        game_over = True
                        print(hangman_stages[attempts])
                        print("You lost! The word was:", word)
                else:
                    print("Correct guess!")
                    if "_" not in display_word(word, guesses):
                        game_over = True
                        print("Congratulations! You won!")
        else:
            print("Invalid input! Please enter a single letter.")
        
        print()
    
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()
    else:
        print("Thank you for playing Hangman!")

# Start the game
play_game()

