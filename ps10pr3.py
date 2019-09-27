#
# ps10pr3.py (Problem Set 10, Problem 3)
#
# Playing the game!
#
# name: Julia Thee
# email: jrmthee@bu.edu
#
# This is an individual-only problem that you must complete on your own,
# without a partner.
#

from ps10pr1 import Board
from ps10pr2 import Player
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One of them should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure that one is 'X' and one is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board):
            return board

        if process_move(player2, board):
            return board


def process_move(player, board):
    """ processes a single move by the specified player on the specified board.
        parameters: Player object: player whose move is being processed
                    Board object: game that is being played
    """
    print(str(player) + "'s turn")
    col = player.next_move(board)
    board.add_checker(player.checker, col)
    print()
    print(board)
    if board.is_win_for(player.checker) == True:
        print(str(player) + ' wins in ' + str(player.num_moves) + ' moves.')
        print('Congratulations!')
        return True
    elif board.is_full() == True:
        print("It's a tie!")
        return True
    return False


class RandomPlayer(Player):
    """ data class representing an unintelligent computer player that choose at random
        from the available columns.
    """
    def next_move(self, board):
        """ overrides (replaces) the next_move method that is inherited from Player
        """
        not_full = []
        for c in range(board.width):
            if board.can_add_to(c) == True:
                not_full += [c]
        self.num_moves += 1
        return random.choice(not_full)
    
        
    
        
        
        








