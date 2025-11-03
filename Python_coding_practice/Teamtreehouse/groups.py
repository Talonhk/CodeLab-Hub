musical_groups = [
    ["Ad Rock", "MCA", "Mike D."],
    ["John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"],
    ["Salt", "Peppa", "Spinderella"],
    ["Rivers Cuomo", "Patrick Wilson", "Brian Bell", "Scott Shriner"],
    ["Chuck D.", "Flavor Flav", "Professor Griff", "Khari Winn", "DJ Lord"],
    ["Axl Rose", "Slash", "Duff McKagan", "Steven Adler"],
    ["Run", "DMC", "Jam Master Jay"],
]
# Loop through the list of musical groups, join members with commas, and print the result
for group in musical_groups:
    # Join the members of the group with commas
    members = ", ".join(group)
    # Print only groups with 3 members
    if len(group) == 3:
        # Print the formatted string with the group members
        print(f"{members} are in a band.")


groceries = ['roast beef', 'potatoes', 'carrots', 'onions', 'celery', 'peas', 'corn', 'green beans']

for index, item in enumerate(groceries):
    print(f'{index}.{item}');


rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
for colors in enumerate(rainbow):
    print(f'{colors}');

for i in range(1, 10):
    print(i);