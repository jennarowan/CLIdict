import json

# Loads in the definitions file as a dict
data = json.load(open("data.json","r"))

def print_definition(user_word):

    # Personal terminal cleanliness preference
    print("")

    # Loops through all possible definitions of the word and prints them
    for definition in data[user_word]:

        print(definition)

# Grabs the word to be looked up
user_word = input("\nPlease enter a word to be defined:\n")

try:
    print_definition(user_word.lower())

except KeyError:
    print("I'm sorry but that word is not in our dictionary.  Please try again.")

# Personal terminal cleanliness preference
print("")