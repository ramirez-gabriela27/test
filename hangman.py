#import libraries
import random

# constants
MAX_GUESSES = 6

# global variables
secret_word = ''
letters_guessed = []
game_over = False


#pick a word
def get_word():
    #words = ["apple", "orange", "python", "happy", "birthday", "random", "life", "string", "list"]

    words = []    
    in_file = open("words.txt", "r")
    for line in in_file:
        words.append(line.strip())

    word = random.choice(words)
    return word

#print our word with letters or '-'
def print_guessed():
    global secret_word, letters_guessed

    for letter in secret_word:
        if letter in letters_guessed:
            print(f"{letter}", end="")
        else:
            print("-", end="")    

#check if player has guessed word, and won game
def check_won():
    global secret_word, letters_guessed
    check = ''
    #iterate through the word
    for letter in secret_word:
        if letter in letters_guessed:
            check += letter
        else:
            check += '-'
    #after creating check, compare and return
    if check == secret_word:
        return True
    else:
        return False

#actually play the game
def play_hangman():
    global secret_word, letters_guessed, game_over

    #keep track of mistakes made
    mistakes_made = 0
    #pick secret word
    secret_word = get_word()

    while game_over == False:
        print("you have %d guesses left." % (MAX_GUESSES - mistakes_made))

        print_guessed()
        print("")

        guess = input("Enter a letter: ").lower()
        #check if letter is already in guessed letters
        while guess in letters_guessed:
            print("You have already guessed letter %s." % guess)
            guess = input("Enter a letter: ").lower()
        letters_guessed.append(guess)

        if check_won():
            print(secret_word)
            print("You won!")
            game_over = True
        else:
            if guess in secret_word:
                continue
            else:
                mistakes_made += 1
                print("There is no %s." % guess)
            if mistakes_made == MAX_GUESSES:
                print("Game Over")
                game_over = True



def main():
    play_hangman()

main()