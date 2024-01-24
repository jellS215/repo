# Sve this as pythonReview.py

# In your own words describe, what a computer program is?

# A computer program is a line of code with set instructions

# In your own words, describe what it mean to call a function? 

# to tell the program to run a block of code

# Create a elevator function that will run specific lines of code 
# based on the conditions provided by a user. If the user types in 101,
# the function should print out they are going to the boys latin office, 
# if they type in 203, they are going to the gym, 
# and if they type in the letter g, the lobby. else, 
# if the input doesnt match any of the values provided, 
# tell the user that floor doesn't exist and to please
# enter a valid floor number.

def elevator():
    floor = input("Where would you like to go? ")
    if floor == "101":
        print("Going to boys latin office")
    elif floor == "203":
        print("Going to the gym")
    elif floor == "g":
        print("Going to Lobby")
    else:
        print("Sorry Wrong Floor, Please enter valid floor number")

elevator()
    

# Create a function that will do the following calculation.
# Your function should take in three argument. it should add the first
# two arguments and then the sum of the first two (2) should be divided 
# by the third argument. You function should then print the result.



