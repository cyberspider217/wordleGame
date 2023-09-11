import random

def give_instructions():
    print('''\n This is a CLI wordle game.
    You have 5 attempts    
    [C] = Letter is correct and in the correct position
    [S] = this letter is somewhere in the word but not in the right position
    [N/A] = This letter is not in the word

    Best of luck''')


words = ["this", "five", "time", "lake", "pink", "help", "tree", "cats", "corf"] # this is a list

hidden_word = random.choice(words) # hidden word variable. Selects a random word from the words variable


def check_word(guess):
    if hidden_word == guess: # checks if guess is equal to the hidden word
        print("Congrats!!! You Did it.")
        print(f"The hidden word was: {hidden_word}")
        return True
    else:
        result = "" # empty string
        for i,j in zip(guess, hidden_word): #goes through each letter of the guess variable and compares it to the hidden word variable. zip function does that
            if i == j:
                result = result + "[C]" # adds to empty string. Keeps everything on same line
            elif i in hidden_word:
                result = result + "[S]"# ^
            else:
                result = result + "[N/A]"# ^
        print(result)
        return False

def main_loop():
    attempt_limit = 5
    give_instructions()
    while attempt_limit > 0:
        guess = input("Enter a 4 letter word: ")
        if check_word(guess): # puts the guess variable into the check word function
            break
        else:
            attempt_limit -= 1 # attempts = attempts - 1
            print(f"You have {attempt_limit} attempts left.")
    else:
        print("")
        print("")
        print("GAME OVER")
        print("")
        print("")
main_loop()

