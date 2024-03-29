######################################################################
# Author: Concepta Njolima    TODO: Change this to your name
# Username: njolimac            TODO: Change this to your username
#
# Assignment: A01
#
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1988 and 1999. Also prints your friend's animal,
# and your compatibility with that friend's animal.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
######################################################################

# Remember to read the detailed notes about each task in the A01 document.

######################################################################
# (Required) Task 1
# TODO Ask user for their birth year
birth_year = int(input("Enter your Year of Birth"))

# TODO Check the year using if conditionals, and print the correct animal for that year.
# See the a01_pets.py for examples


if birth_year== 1997:
    print(" You are an Ox")
elif birth_year == 1998:
    print(" You are an Tiger")
elif birth_year == 1999:
    print(" You are a Rabbit")
elif birth_year == 2000:
    print(" You are a Dragon")
elif birth_year == 2001:
    print(" You are a snake")
elif birth_year == 2002:
    print(" You are a Horse")
elif birth_year == 2003:
    print(" You are a Goat")
elif birth_year == 2004:
    print(" You are a Monkey")
elif birth_year == 2005:
    print(" You are a Rooster")
else:
    print("Enter a year between 1997 and 2005 ")

######################################################################
# (Required) Task 2
# TODO Ask the user for their friend's birth year
friend_birth = int(input("Enter your friend's year of birth"))


# TODO Similar to above, check your friend's year using if conditionals, and print the correct animal for that year

if friend_birth== 1997:
    print(" Your friend an Ox")
elif friend_birth == 1998:
    print(" Your friend an Tiger")
elif friend_birth == 1999:
    print(" Your friend a Rabbit")
elif friend_birth == 2000:
    print(" Your friend a Dragon")
elif friend_birth == 2001:
    print(" Your friend is a snake")
elif friend_birth == 2002:
    print(" Your friend is a Horse")
elif friend_birth == 2003:
    print(" Your friend is a Goat")
elif friend_birth == 2004:
    print(" Your friend is  a Monkey")
elif friend_birth == 2005:
    print(" Your friend a Rooster")
else:
    print("Enter a year between 1997 and 2005 ")

######################################################################
# (Optional) Task 3
# TODO Check for compatibility between your birth year and your friend's birth year
# NOTE: You can always assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.
if birth_year == 1997 and friend_birth == 1997 or friend_birth == 2001 or friend_birth == 2005:
    print("Great friends!!! hahahaaahaha")

elif birth_year== 2003:
    print("Goat!!! Got all reasons to keep away from me!")

# TODO print if you are a strong match, no match, or in between
