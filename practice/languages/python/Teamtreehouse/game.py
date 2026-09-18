from cards import Card
import random
import json
import os
import time

# High score and difficulty utilities
HIGHSCORE_FILE = os.path.join(os.path.dirname(__file__), 'highscores.json')
MAX_SCORES = 10

CARD_VOCAB = ['Add','Boo','Cat','Dev','Egg','Far','Gum','Hut','Ice','Jet','Key','Log','Map','Net','Oak','Pig','Queen','Run','Sun','Top','Urn','Van','Web','Yak','Zen','Arc','Box','Cry','Den','Elm','Fox']

def load_high_scores():
    try:
        with open(HIGHSCORE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"easy": [], "medium": [], "hard": []}
    except Exception:
        return {"easy": [], "medium": [], "hard": []}

def save_high_scores(data):
    try:
        with open(HIGHSCORE_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
    except Exception:
        # don't crash on write errors
        pass

def update_high_scores(difficulty, name, score):
    data = load_high_scores()
    scores = data.get(difficulty, [])
    scores.append({"name": name, "score": score})
    scores = sorted(scores, key=lambda x: x["score"], reverse=True)[:MAX_SCORES]
    data[difficulty] = scores
    save_high_scores(data)

def show_high_scores(difficulty):
    data = load_high_scores()
    scores = data.get(difficulty, [])
    if not scores:
        print(f"No high scores yet for {difficulty}.")
        return
    print(f"High scores ({difficulty}):")
    for i, rec in enumerate(scores, start=1):
        print(f"{i}. {rec['name']} — {rec['score']}")

def choose_difficulty():
    while True:
        s = input("Choose difficulty (easy / medium / hard) [medium]: ").strip().lower() or 'medium'
        if s in ("easy", "medium", "hard"):
            return s
        print("Please type 'easy', 'medium' or 'hard'.")

def difficulty_to_size(difficulty):
    if difficulty == 'easy':
        return 2
    if difficulty == 'medium':
        return 4
    if difficulty == 'hard':
        return 6
    # default to medium if an unexpected value is passed
    return 4

def card_options_for_size(size):
    pairs = (size * size) // 2
    if pairs > len(CARD_VOCAB):
        raise RuntimeError("Not enough unique card labels for this difficulty.")
    return random.sample(CARD_VOCAB, pairs)

def compute_score(moves, seconds, pairs):
    base = pairs * 1000
    penalty = int(moves * 20 + seconds * 5)
    return max(0, base - penalty)


class Game:
    def __init__(self):
        self.size = 4
        self.card_options = ['Add', 'Boo', 'Cat', 'Dev',  'Egg', 'Far', 'Gum', 'Hut']
        self.columns = ['A', 'B', 'C', 'D']
        self.cards = []
        self.locations = []
        for column in self.columns:
            for num in range(1, self.size + 1):
                location = f'{column}{num}'
                self.locations.append(location)
    # Methods

    def set_cards(self):
        used_locations = []
        for card in self.card_options:
            for i in range(2):
                avilable_locations = set(self.locations) - set(used_locations)
                random_location = random.choice(list(avilable_locations))
                used_locations.append(random_location)
                game_card = Card(card, random_location)
                self.cards.append(game_card)
        if len(self.cards) != len(self.locations):
            raise RuntimeError("Unexpected number of cards placed.")

    def create_row(self, num):
        row = []
        for column in self.columns:
            found = False
            for card in self.cards:
                if card.location == f'{column}{num}':
                    found = True
                    if card.matched:
                        row.append(str(card))
                    else:
                        row.append('   ')
                    break
            if not found:
                # keep the grid aligned even if a card is missing
                row.append('   ')
        return row

    def create_grid(self):
        header = ' |  ' + '  |  '.join(self.columns) + '  |'
        print(header)
        # ensure self.size is an integer (fallback to 0 if None)
        size = int(self.size) if self.size is not None else 0
        for row in range(1, size + 1):
            print_row = f'{row}| '
            get_row = self.create_row(row)
            print_row += ' | '.join(get_row) + ' |'
            print(print_row)
    
    # check for matches
    def check_match(self, loc1, loc2):
        # guard against identical locations
        if loc1 == loc2:
            print("Cannot match the same location twice.")
            return False

        first = next((c for c in self.cards if c.location == loc1), None)
        second = next((c for c in self.cards if c.location == loc2), None)

        if first is None or second is None:
            print("One of the selected locations did not resolve to a card. Try again.")
            return False

        if first == second:
            first.matched = True
            second.matched = True
            return True

        # not a match — show both cards to the player
        print(f'{first.location}: {first}')
        print(f'{second.location}: {second}')
        return False
            
        # check for a win
    def check_win(self):
        for card in self.cards:
            if not card.matched:
                return False
        return True
        
        # make sure the player’s location input is a real
    def check_location(self, time):
        while True:
            guess = input(f"What's the location of your {time} card? ")
            if guess.upper() in self.locations:
                return guess.upper()
            else:
                print("That's not a vaild location. It should look like this: A1")
                    
        # run the game
    def start_game(self):
        # Choose difficulty and initialize board
        difficulty = choose_difficulty()
        size = difficulty_to_size(difficulty)
        self.size = size
        self.columns = [chr(ord('A') + i) for i in range(size)]
        self.locations = [f"{c}{r}" for c in self.columns for r in range(1, size + 1)]
        self.card_options = card_options_for_size(size)

        pairs = (size * size) // 2
        moves = 0
        start_time = time.time()

        game_running = True
        print('Guess the Cards')
        self.set_cards()
        try:
            while game_running:
                self.create_grid()
                guess1 = self.check_location('first')
                while True:
                    guess2 = self.check_location('second')
                    if guess2 == guess1:
                        print("You selected the same location twice — please choose a different second card.")
                    else:
                        break

                moves += 1

                if self.check_match(guess1, guess2):
                    if self.check_win():
                        elapsed = int(time.time() - start_time)
                        score = compute_score(moves, elapsed, pairs)
                        print('Congrats!! You have guessed them all')
                        self.create_grid()
                        print(f'You took {moves} moves and {elapsed} seconds. Score: {score}')
                        name = input('Enter your name to save the high score (or leave blank): ').strip()
                        if name:
                            update_high_scores(difficulty, name, score)
                            show_high_scores(difficulty)
                        game_running = False
                else:
                    input('Those cards are not a match. Press Enter to continue')
        except (KeyboardInterrupt, EOFError):
            print("\nGame aborted.")
        print('Game Over')
                            

# dunder main
    # create an instance
if __name__ == '__main__':
    game = Game()                              
    # call start game
    game.start_game()