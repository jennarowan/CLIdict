import json
from difflib import get_close_matches

# Loads in the definitions file as a dict
data = json.load(open("data.json","r"))

# Housekeeping to make program run until user chooses to exit
loop = True

def print_definition(user_word):

    # This function loops through all possible definitions of the word and prints them    

    # Personal terminal cleanliness preference
    print("")

    for definition in data[user_word]:

        print(definition)

def no_match(user_word):

    # This function runs when the input isn't in the definition file
    print(f"\nI'm sorry but {user_word} does not exist in our dictionary.")

def check_user_word(user_word):

    # This function attempts to find the definition in the data file and print it.
    # If the word does not exist it attempts to find a close match.  If a close match
    # found it asks the user whether they meant the match.

    try:
        print_definition(user_word)

    except KeyError:

        # Checks to see if capitilization is the problem, recurses with the corrected word if so
        if user_word.lower() in data:

            check_user_word(user_word.lower())
            return

        elif user_word.title() in data:

            check_user_word(user_word.title())
            return

        elif user_word.upper() in data:

            check_user_word(user_word.upper())
            return

        # Checks to see if a close match exists, in case of fat fingers
        possible_word = get_close_matches(user_word, data, 1)

        if possible_word:

            # If close match exists, did the user mean that word?
            grabMatch = input(f"Did you possibly mean to type {possible_word[0]}?  Y/N: ")

            if grabMatch.lower() == "y":

                # If the user meant to type that word we start again with that word instead
                check_user_word(possible_word[0])

            else:

                no_match(user_word)

        else:

            no_match(user_word)

while loop:

    # Grabs the word to be looked up
    user_word = input("\nPlease enter a word to be defined:\n")

    check_user_word(user_word)

    # Determines whether to loop to search for another word
    go_again = input("\nWould you like to look up another word?  Y/N: ")

    # Ends program
    if go_again.lower() != "y":

        loop = False

# Personal terminal cleanliness preference
print("")