#
# Julia Thee
# jrmthee94@gmail.com
# Connect Four Board class
#


class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """
    def __init__(self, height, width):
        """ a constructor for Board objects """
        self.height = height
        self.width = width
        self.slots = [[' '] * width for row in range(self.height)]


    def __repr__(self):
        """ returns a string representation of a Board """
        s = ''              # begin with an empty string
        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'
        s += '-' * self.width*2 + '-'
        s += '\n'
        for i in range(self.width):
            nums = str(i%10)
            s += ' ' + nums
        return s

    def add_checker(self, checker, col):
        """ accepts two inputs, checker and col, and adds the checker to the appropriate row in column col of the board.
            input: checker: one-character string ('X' or 'O') that specifies the checker to add to the board.
                   col: integer that specifies the index of the column to add the checker.
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        row = 0
        while (row <= (self.height-2)) and (self.slots[row+1][col] == ' '):
            row += 1
        self.slots[row][col] = checker


    def clear(self):
        """ clears the Board object on which it is called by setting all slots to contain a space character.
        """
        self.slots = [[' '] * self.width for row in range(self.height)]


    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'


    def can_add_to(self, col):
        """ returns True if it is valid to place a checker in the column on the calling Board object,
            otherwise returns False.
            input: col must be in range from 0 to the last column on the board, and specified column cannot be full.
        """
        if col >= 0 and col < self.width:
            if self.slots[0][col] == ' ':
                return True
            return False
        return False



    def is_full(self):
        """ returns True if the called Board object is completely full of checkers,
            and returns False otherwise.
        """
        for c in range(self.width):
            if self.can_add_to(c) == True:
                return False
        return True



    def remove_checker(self, col):
        """ removes the top checker from column col of the called Board object.
            If column is empty, do nothing.
        """
        row = 0
        if col >= 0 and col < self.width:
            while row < (self.height - 1) and self.slots[row][col] == ' ':
                row += 1
            self.slots[row][col] = ' '



    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False



    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """
        for row in range(self.height-3):
            for col in range(self.width):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col] == checker and \
                   self.slots[row+2][col] == checker and \
                   self.slots[row+3][col] == checker:
                    return True

        # if we make it here, there were no vertical wins
        return False



    def is_down_diagonal_win(self, checker):
        """ Checks for a down diagonal win for the specified checker.
        """
        for row in range(3, self.height):
            for col in range(self.width-3):
                # Check if the next four columns in this diagonal row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row-1][col+1] == checker and \
                   self.slots[row-2][col+2] == checker and \
                   self.slots[row-3][col+3] == checker:
                    return True

        # if we make it here, there were no down diagonal wins
        return False



    def is_up_diagonal_win(self, checker):
        """ Checks for an up diagonal win for the specified checker.
        """
        for row in range(self.height-3):
            for col in range(self.width-3):
                # Check if the next four columns in this diagonal row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col+1] == checker and \
                   self.slots[row+2][col+2] == checker and \
                   self.slots[row+3][col+3] == checker:
                    return True

        # if we make it here, there were no up diagonal wins
        return False
    


    def is_win_for(self, checker):
        """ returns True if there are four of the same checkers in a row, in either a vertical, horizontal, or diagonal fashion.
            input: checker is a one character string, either an 'X' or 'O'
        """
        assert(checker == 'X' or checker == 'O')

        if self.is_horizontal_win(checker) == True or  \
           self.is_vertical_win(checker) == True or \
           self.is_down_diagonal_win(checker) == True or \
           self.is_up_diagonal_win(checker) == True:
            return True
        return False


        
                

        

        





        
