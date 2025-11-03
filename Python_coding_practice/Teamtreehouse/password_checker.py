import sys

MASTER_PASSWIRD = 'opensesame'
password = input("Please enter the super sercet password:  ")
attempt_count = 1
while password != MASTER_PASSWIRD: 
    if attempt_count > 3:
        sys.exit("To many invalid attempts")
    password = input("Invalid password, try again:  ")
    attempt_count += 1
print("welcome to serecttown")