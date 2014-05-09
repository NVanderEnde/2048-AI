import random

import square


class Board(object):
    """
	Describes a board of 2048 - a 4x4 collection of Squares
	"""

    def __init__(self):
        """
		Creates a new board with two valued squares and 14 zero'd squares
		"""
        self.board_size = 4
        self.Squares = [square.Square() for i in range(self.board_size ** 2)]
        #Give two squares an initial value
        for i in range(2):
            sq = self.get_random_unassigned_square()
            sq.set_random_value()
        print(square.value for square in self.Squares)

    def get_random_unassigned_square(self):
        """
		Return a randomly-selected, zero'd square from this board
		or None if there are no zero'd squares
		"""
        free_squares = [square for square in self.Squares if square.value is 0]
        return random.choice(free_squares) if len(free_squares) > 0 else None

    def board_is_full(self):
        return self.get_random_unassigned_square() is None

    def get_square(self, x, y):
        return self.square_board()[x][y]

    def get_column(self, row_index):
        return [self.square_board()[row_index][i] for i in range(self.board_size)]

    def square_board(self):
        """
		Returns a 4x4 squared board
		"""
        list_to_return = []
        for i in range(self.board_size):
            list_to_append = []
            for k in range(self.board_size):
                list_to_append.append(self.Squares[4 * i + k])
            list_to_return.append(list_to_append)

        return list_to_return

