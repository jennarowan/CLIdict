import json

# Loads in the definitions file as a dict
data = json.load(open("data.json","r"))

# Grabs the word to be looked up
userWord = input("\nPlease enter a word to be defined:\n")

print(f"\nThe defintion(s) of {userWord}:\n")

# Loops through all possible definitions of the word and prints them
for definition in data[userWord]:

    print(definition)

print("")