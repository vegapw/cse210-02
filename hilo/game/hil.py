import random


class Hil:
    """A set of cards from 1 to 13

    The responsibility of Hil is to keep track of the current card and calculate the points depending
    if the guess is correct or not.
   
    Attributes:
        card (int): The number of the current card
        points (int): The number of points accumulated starting with 300.
    """

    def __init__(self):
        """Constructs a new instance of Hil with a card and points attribute.

        Args:
            self (Hil): An instance of Hil.
        """
        self.card = 0
        self.points = 300

    def get_card(self):
        """Generates a new random card.
        
        Args:
            self (Hil): An instance of Hil.
        """
        self.card = random.randint(1,13)
    
    def guessed(self):
        """Increase the points by 100.
        
        Args:
            self (Hil): An instance of Hil.
        """
        self.points += 100
    

    def not_guessed(self):
        """Decrease the points by 75.
        
        Args:
            self (Hil): An instance of Hil.
        """
        self.points -= 75
