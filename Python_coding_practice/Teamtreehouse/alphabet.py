## Challenge ##
# Write code to find the word in a 
# list that would come first alphabetically

## Example: When given the list below
# word_list = ["hamster", "turtle", "cat", "bird"]
# The code should find "bird" as the word that 
# would come first alphabetically



def word_alphabetically():
    word_list = ["hamster", "turtle", "cat", "bird"]
    print("The first word alphabetically is: " + min(word_list))
    return min(word_list)
   
def last_name_alphabetically():
    last_names = ["Rodriguez", "Lee", "Yakinian", "Amendola"]
    # Sort the list alphabetically
    print("The first last name alphabetically is: " + min(last_names))
    return min(last_names)

def main():
    # Define the lists
    word_alphabetically()
    last_name_alphabetically()


if __name__ == "__main__":
    print(main())

