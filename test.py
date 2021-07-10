# This file is just for testing random bits of code before merging them into main.py

import mysql.connector

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
    )

cursor = con.cursor()

word=input("Enter the word: ")

query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()

if results:

    for result in results:
        print(result[0])

else:

    query = cursor.execute("SELECT Expression FROM Dictionary WHERE SOUNDEX(Expression) = SOUNDEX('%s') LIMIT 1" % word)
    possible_word = cursor.fetchall()
    print(possible_word[0][0])