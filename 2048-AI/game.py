from board import Board
from square import Square


class Game(object):
    """
	A single game of 2048 - contains the board and functions which manipulate it
	"""

    def __init__(self):
        """
		Instantiate a new board
		"""
        self.GameBoard = Board()
        self.Score = 0
        self.GameWon = False


    def move_board(self, direction):
        """
		Move the board in one of the four possible directions.
		"""
        vector = direction.vector()
        vector_x = vector[0]
        vector_y = vector[1]
        moveRow = vector_x != 0
        moveColumn = vector_y != 0
        if (moveRow and moveColumn):
            raise Exception("Can't move both a row and a column at the same time!")
        before_move = self.GameBoard
        if moveRow:
            for row in self.GameBoard.square_board():
                row = self.execute_move(row, vector_x)
        elif moveColumn:
            for i, row in enumerate(self.GameBoard.square_board()):
                column = self.GameBoard.get_column(i)
                column = self.execute_move(column, vector_y)
        if before_move != self.GameBoard:
            #Only add a new square if the move was successful
            self.GameBoard.get_random_unassigned_square().set_random_value()


    def execute_move(self, line, direction):
        """
		Move a line (row or column) in the specified direction.
		Then handle the resulting collisions.
		Then move it again (to ensure that merges without obstacles end up on the other side)
		"""
        line = self.move_line(line, direction)
        line = self.handle_collisions(line, direction)
        line = self.move_line(line, direction)
        return line


    def move_line(self, line, direction):
        new_line = [square for square in line if square.value != 0]
        new_empty_squares = [Square()] * (self.GameBoard.board_size - len(new_line))
        if (direction > 0):
            return new_empty_squares + new_line
        else:
            return new_line + new_empty_squares


    def handle_collisions(self, line, direction):
        if (direction > 0):
            range_to_iterate_line = range(0, self.GameBoard.board_size - 1, direction)
        else:
            range_to_iterate_line = range(self.GameBoard.board_size - 1, 0, direction)

        for index in range_to_iterate_line:
            if (line[index].value is 0):
                continue
            if (self.collision_is_match(line[index], line[index + direction])):
                new_value = line[index].value + line[index + direction].value
                if (new_value == 2048):
                    self.GameWon = True
                line[index].value = new_value
                line[index + direction].value = 0
                self.Score += new_value
        return line

    def collision_is_match(self, first_square, second_square):
        return first_square.value == second_square.value


class Direction(object):
    """
	Defines directions in which the board can move
	"""

    def __init__(self, value):
        value = int(value)
        if 0 > value > 4:
            raise Exception("Only Cardinal directions are supported!")
        self.value = value
        #Keys: up, right, down left. Values: x, y pairs
        self.vector_table = {
            0: (0, -1),
            1: (1, 0),
            2: (0, 1),
            3: (-1, 0)
        }

    def vector(self):
        return self.vector_table[self.value]
