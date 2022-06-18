from game.hil import Hil


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        hil = Hil()
        hil.get_card()
        while self.is_playing:

            print(f"\nThe card is: {hil.card}")
            choice = input("Higher or lower? [h/l] ")
            previous_card = hil.card
            hil.get_card()
            print(f"Next card was: {hil.card}")
            if hil.card > previous_card and choice.lower() == "h":
                hil.guessed()
            elif hil.card < previous_card and choice.lower() == "l":
                hil.guessed()
            else:
                hil.not_guessed()
            if hil.points > 0:
                print(f"Your score is: {hil.points}")
                self.get_inputs()
            else:
                self.is_playing = False
        print("Game over\n")


    def get_inputs(self):
        """Ask the user if they want to continue.

        Args:
            self (Director): An instance of Director.
        """

        play_again = input("Play again? [y/n] ")
        self.is_playing = (play_again.lower() == "y")
       
    