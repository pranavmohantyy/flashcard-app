class Flashcard:
    def __init__(self, front, back, difficulty):
        self.front = front
        self.back = back
        self.difficulty = difficulty

class Deck:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def list_cards(self):
        return [(card.front, card.back, card.difficulty) for card in self.cards]

    def quiz(self):
        for card in self.cards:
            input(f"{card.front} (press enter to reveal)")
            print(card.back)
            correct = input("Was that correct? (y/n): ").strip().lower()
            if correct == 'y':
                print("Great!")
            else:
                print("No worries, keep practicing!")