#
# Julia Thee
# jrmthee94@gmail.com
# Connect Four AI Player class
#

from ps10pr3 import *
import random

class AIPlayer(Player):
    """ data class representing a more intelligent computer player- one that uses
        techniques from artificial intelligence to choose its next move.
    """
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        Player.__init__(self, checker)
        self.tiebreak = str(tiebreak)
        self.lookahead = lookahead


    def  __repr__(self):
        """ returns a string representing an AIPlayer object.
        """
        return 'Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'


    def max_score_column(self, scores):
        """ returns the index of the column with the maximum score, applying the tiebreaking
            strategy if there is a tie between columns.
            input 'scores': list containing a score for each column of the board.
        """
        max_score = max(scores)
        list_max = []
        for i in range(len(scores)):
            if scores[i] == max_score:
                list_max += [i]
        if len(list_max) == 1:
            return list_max[0]
        elif self.tiebreak == 'LEFT':
            return list_max[0]
        elif self.tiebreak == 'RIGHT':
            return list_max[-1]
        return random.choice(list_max)


    def scores_for(self, board):
        """ determines the called AIPlayer's scores for the columns in board
        """
        scores = [50] * board.width
        for c in range(board.width):
            if board.can_add_to(c) == False:
                scores[c] = -1
            elif board.is_win_for(self.checker) == True:
                print("100!!!")
                scores[c] = 100
            elif board.is_win_for(self.opponent_checker()) == True:
                print("0!!!")
                scores[c] = 0
            elif self.lookahead == 0:
                scores[c] = 50
            else:
                board.add_checker(self.checker,c)
                print("BOARD")
                print(board)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, (self.lookahead - 1))
                opp_scores = opponent.scores_for(board)
                print(opp_scores)
                if max(opp_scores) == 0:
                    scores[c] = 100
                elif max(opp_scores) == 100:
                    scores[c] = 0
                elif max(opp_scores) == 50:
                    scores[c] = 50
                board.remove_checker(c)
        return scores


    def next_move(self, board):
        """ overrides (replaces) the next_move method that is inherited from Player.
        """
        scores = self.scores_for(board)
        self.num_moves += 1
        return self.max_score_column(scores)


# run game: connect_four(Player('X'),AIPlayer('O', 'RANDOM', 3))

connect_four(Player('X'),AIPlayer('O', 'RANDOM', 3))

#connect_four(Player('X'),Player('O'))







        




        

