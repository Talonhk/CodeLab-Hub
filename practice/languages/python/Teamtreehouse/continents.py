continents = [
    'Asia',
    'South America',
    'North America',
    'Africa',
    'Europe',
    'Antarctica',
    'Australia',
]
# Your code here
print("Continents:")
for continent in continents:
    if continent[0] == 'A':
        print("* " + continent)

#------------------------------------------------------------------------------------


books = [
    "Learning Python: Powerful Object-Oriented Programming - Mark Lutz",
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis - Wes McKinney",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]
video_games = [
    "The Legend of Zelda: Breath of the Wild",
    "Splatoon 2",
    "Super Mario Odyssey",
]

def display_wishlist(display_name, wishes):
  print(display_name + ":")
  suggested_gift = wishes[0]
  print("====>", suggested_gift, "<====")
  for wish in wishes:
    print("* " + wish)
  print()
  
display_wishlist("Books", books)
display_wishlist("Video Games", video_games)
         