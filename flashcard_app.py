import json
import os

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
            correct = input("Was that correct? (y/n) ").lower()
            if correct == 'y':
                card.difficulty += 1
            else:
                card.difficulty = max(0, card.difficulty - 1)

    def save_deck(self):
        deck_path = os.path.expanduser("~/.flashcards/")
        os.makedirs(deck_path, exist_ok=True)
        with open(os.path.join(deck_path, self.name + '.json'), 'w') as f:
            json.dump(self.list_cards(), f)

    @classmethod
    def load_deck(cls, name):
        deck_path = os.path.expanduser("~/.flashcards/")
        with open(os.path.join(deck_path, name + '.json'), 'r') as f:
            cards = json.load(f)
            deck = cls(name)
            for front, back, difficulty in cards:
                deck.add_card(Flashcard(front, back, difficulty))
            return deck