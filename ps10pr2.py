#
# Julia Thee
# jrmthee94@gmail.com
# Connect Four Player class
#

from ps10pr1 import Board

# Write your Player class below.

class Player:
    """ a data class representing a player of the Connect Four game
    """

    def __init__(self, checker):
        """ constructs a new Player object """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0


    def  __repr__(self):
        """ returns a string representing a Player object, indicating which
            checker the Player object is using.
        """
        return 'Player ' + self.checker


    def opponent_checker(self):
        """ returns a one-character string representing the checker of the Player object's opponent.
            Player checker is either 'X' or 'O'
        """
        if self.checker == 'X':
            return 'O'
        return 'X'


    def next_move(self, board):
        """ accepts a Board object as a parameter and returns the column where
            the player wants to make the next move.
        """
        col = int(input('Enter a column: '))
        while True:
            if board.can_add_to(col) == True:
                self.num_moves += 1
                return col
            print('Try again!')
            col = int(input('Enter a column: '))
            
        




        
