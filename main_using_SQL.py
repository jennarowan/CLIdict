# THIS VERSION OF THE FILE SWAPS OUT THE LOCAL JSON FILE
# AND RELATED HANDLING IN FAVOR OF A REMOTE DATABASE ACCESSED
# USING MySQL

import mysql.connector

# Database and credentials provided by teacher who made the
# tutorial I used for this program
con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
    )

cursor = con.cursor()

# Housekeeping to make program run until user chooses to exit
loop = True

def no_match(user_word):

    # This function runs when the word isn't in the database
    print(f"\nI'm sorry but {user_word} does not exist in our dictionary.")

def check_user_word(user_word):

    # This function attempts to find the definition in the database and print it.
    # If the word does not exist it attempts to find a close match.  If a close match
    # found it asks the user whether they meant to enter the match.

    query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % user_word)
    results = cursor.fetchall()

    if results:

        # Personal terminal cleanliness preference
        print("")

        # Prints whatever number of definitions exist for the word
        for definition in results:

            print(definition[0])

    else:

        # Tries to find a near match
        check_close_matches(user_word)

def check_close_matches(user_word):

    # This function searches the database for any word close to the input from the user
    # If found the user will be asked if that word is what they really meant
    query = cursor.execute("SELECT Expression FROM Dictionary WHERE SOUNDEX(Expression) = SOUNDEX('%s') LIMIT 1" % user_word)
    possible_word = cursor.fetchall()

    if possible_word:

        # If close match exists, did the user mean that word?
        grabMatch = input(f"\nDid you possibly mean to type {possible_word[0][0]}?  Y/N: ")

        if grabMatch.lower() == "y":

            # If the user meant to type that word we start again with that word instead
            check_user_word(possible_word[0][0])

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