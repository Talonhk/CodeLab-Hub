import math
# This program will split a check between a number of people
# It will ask for the total amount of the check and the number of people
# It will then calculate the amount each person owes


def split_check(total, number_of_people):
    if number_of_people < 2:
        raise ValueError("More than 1 person is required to split the check.")
    return math.ceil(total / number_of_people)

try:
    # Ask the user for the total amount of the check
    total_due = float(input("what is the total dollar amount?"))
    number_of_people = int(input("how many peopleare we spliting the check for?"))
    amount_due = split_check(total_due, number_of_people)
except ValueError as err:
    print("Oh no! That is not a Dollar amount. Try again...")
    print("({})".format(err))
else:
    print("Each person owes ${}".format(amount_due))

#------------------------------------------------------------

