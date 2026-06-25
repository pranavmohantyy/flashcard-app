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