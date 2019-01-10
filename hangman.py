import random


# WELCOME THE USER!
def welcome_message():
    while True:
        name = input("Enter your name:\n")

        if name.isspace():
            print("Please enter your name , do not leave it blank!\n")
        else:
            break
    print("#################~~HANGMAN~~######################")
    print("WELCOME," + name.upper() + ". LET'S PLAY HANGMAN")
    print("##################################################\n")

welcome_message()
words_list = ("audi mercedes-benz toyota bmw honda peugeot proton").upper().split()
# COMPUTER WILL CHOOSE SECRET WORD FROM THE WORDS LIST
secret_word = random.choice(words_list)
correct = []
incorrect = []

hangman_body = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
# STARTING HANGMAN
def hangman():

    print("SO THE WORD YOU NEED TO GUESS HAS " + str(len(secret_word)) + " CHARACTERS\n")
    print(hangman_body[len(incorrect)])
    for i in secret_word:
        if i in correct:
            print(i, end=" ")
        else:
            print("_", end=" ")
    print("\n")
    print("************WRONG LETTERS************")
    print(incorrect)
    print("*************************************")

def check_users_guess():

    while True:
        user_input = input("\n\nTake a guess: ").upper()
        if len(user_input) > 1:
            print("Enter a single letter. Please try again!")
        elif user_input in correct or user_input in incorrect:
            print("You have already guessed that word, please try again.")
        elif user_input.isspace():
            print("Please try again!")
        elif user_input.isnumeric():
            print("please enter a letter")
        else:
            break

    if user_input in secret_word:
        correct.append(user_input)
        print("\n\nThat's right, you have guessed it correctly!")
    else:
        incorrect.append(user_input)
        print("Try again!")

def win_loss():

    if len(incorrect) == 6:
        return "GAME OVER!!!"
    for i in secret_word:
        if i not in correct:
            return "NO WIN!"
    return "WIN!"
while True:
    hangman()
    check_users_guess()
    result = win_loss()

    if win_loss() == "GAME OVER!!!":
        print("DEFEAT! THE WORD WAS " + secret_word + ".")
        print(hangman_body[len(incorrect)])
        break
    elif win_loss() == "WIN!":
        print(secret_word)
        print("VICTORY!")
        break


