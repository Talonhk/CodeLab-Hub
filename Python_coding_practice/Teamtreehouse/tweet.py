"""
This is importing a function named `tweet` from a file
    that we unfortunately don't have access to change.

You use it like so:
>>> tweet("Hello this is my tweet")

If the function cannot connect to Twitter,
    the function will raise a `CommunicationError`
If the message is too long,
    the function will raise a `MessageTooLongError`
"""
from twitter import (
    tweet,
    MessageTooLongError,
    CommunicationError,
)


message = input("What would you like to tweet?  ")
# call the tweet function and pass in the message that the user enters?
try:
    tweet(message)
except CommunicationError:
    print("An {} occurred attempting to connect to Twitter. Please try again!")
except MessageTooLongError as err:
       print("Oh no! Your message was too long ({})".format(err))

# print("Your message was sent successfully!")

#------------------------------------------------------------   

name = input("What's your name? ")

# TODO: Ask the user by name if they understand Python while loops
print("Hello {}! Do you understand Python while loops?".format(name))


# TODO: Write a while statement that checks if the user doesn't understand while loops
# and if so, ask them again if they understand while loops.
while True:
    answer = input("Do you understand while loops? (Y/N) ")
    if answer.lower() == "y":
        break
    else:
        print("That's okay! Let's try again.")

# TODO: Since the user doesn't understand while loops, let's explain them.
# A while loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition.
# It continues to execute as long as the condition is true.
# In Python, the syntax is as follows:
# while condition:
#     # code block to execute
#
# For example, if you want to print numbers from 1 to 5, you can use a while loop like this:
# number = 1
# while number <= 5:
#     print(number)
#     number += 1
# This will print the numbers 1 to 5, and then stop when the condition is no longer true.
#
# You can also use a while loop to ask the user for input until they provide a valid response.
# For example:
# user_input = ""
# while user_input != "exit":
#     user_input = input("Type 'exit' to quit: ")


# TODO: Ask the user again, by name, if they understand while loops.

  
# TODO: Outside the while loop, congratulate the user for understanding while loops
# TODO: Ask the user by name if they understand Python while loops
understanding = input("{}, do you understand Python while loops?/n(Enter yes/no)".format(name))

#print("Hello {}! Do you understand Python whileloops?".format(name)

# TODO: Write a while statement that checks if the user doesn't understand while loops
while understanding.lower() != 'yes':
  # TODO: Since the user doesn't understand while loops, let's explain them.
  print("Ok, {}, while loops in Python repeat as Long as a certaion Boolean condition is met.".format(name))
  # TODO: Ask the user again, by name, if they understand while loops.
  understanding = input("{}, now do you understand Python while loops?(Enter yes/no)".format(name))

# TODO: Outside the while loop, congratulate the user for understanding while loops
print("That's great, {}. I'm pleased that you understand while loops now. That was getting repetitive.".format(name))