
class Card:
    suits = ["pik", "kier", 
            "karo", "trefl"]
    values = [None, None,"2", "3", "4", 
              "5", "6", "7", "8", "9", "10", 
              "waleta", "damę", "króla", "asa"]

    def __init__(self, value, suit):
        """listy suit i value to liczby całkowite"""
        self.value = value
        self.suit = suit

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        return self.values[self.value] 
               + " " 
               + self.suits[self.suit]
