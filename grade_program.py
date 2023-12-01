#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Dec/1/2023
# This program gets a level from the user (1,2,3,4) and will display
# the middle percentage mark for that level, using a switch statement.

# Creating a function that will find the middle mark percentage of the level entered.


def calc_mark(level):
    # Initializing the mark to 0.
    middle_mark = 0

    # Using the version of a switch statement in python to find the level's middle mark.
    match level:
        case "4++":
            middle_mark = 99
        case "4+":
            middle_mark = 96
        case "4":
            middle_mark = 90
        case "4-":
            middle_mark = 84
        case "3+":
            middle_mark = 78
        case "3":
            middle_mark = 74
        case "3-":
            middle_mark = 71
        case "2+":
            middle_mark = 68
        case "2":
            middle_mark = 64
        case "2-":
            middle_mark = 61
        case "1+":
            middle_mark = 58
        case "1":
            middle_mark = 54
        case "1-":
            middle_mark = 51
        # If the user's input is invalid (didn't enter anything for the level)
        case _:
            middle_mark = -1

    # Returns the value of the mark to my main() function.
    return middle_mark


# My main() function.
def main():
    # Getting user input for their level.
    user_level = input("Enter a level (ex:1,2,3,4): ")

    # Calling calc_mark function to display the middle mark of the user's level.
    user_mark = calc_mark(user_level)

    # Using an if statement to check if the input is invalid.
    if user_mark == -1:
        print("{} is an invalid input. Please try again.".format(user_level))
    # Using an else to display the middle mark, since the user input would be valid.
    else:
        print(
            "The level {} has a middle percentage mark of {} %".format(
                user_level, user_mark
            )
        )


if __name__ == "__main__":
    main()
