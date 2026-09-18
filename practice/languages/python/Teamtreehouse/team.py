# TODO Create an empty list to maintain the player names
player_list = []

# TODO Ask the user if they'd like to add players to the list.
# If the user answers "Yes", let them type in a name and add it to the list.
# If the user answers "No", print out the team 'roster'
add_player = input("Would you like to add players to the team? (yes/no): ")
while add_player.lower() in ["yes", "y"]:
    name = input("\nEnter the player to add to the team: ")
    player_list.append(name)
    add_player = input("Would you like to add another player? (yes/no): ")

# TODO print the number of players on the team
print("\nThere are {} of players on the team.".format(len(player_list)))  

# TODO Print the player number and the player name
# The player number should start at the number one
play_number = 1
for player in player_list:
    print("Player{}: {}".format(play_number, player))
    play_number += 1


# TODO Select a goalkeeper from the above roster
goalkeeper = input("Please select a goalkeeper by entering their player number: (1-{})".format(len(player_list)))

goalkeeper = int(goalkeeper)


# TODO Print the goal keeper's name
# Remember that lists use a zero based index
print("Great!!! The Goalkeeper for the game will be {}".format(player_list[goalkeeper - 1]))
