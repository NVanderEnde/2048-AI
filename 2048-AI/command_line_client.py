from game import Game, Direction

def main():
	game = Game()
	game_loop(game)


def game_loop(game):
	while(True):
		pretty_print(game.GameBoard.square_board())
		key_press = input("Direction?")
		if (key_press == "q"):
			break
		direction = Direction(key_press)
		game.move_board(direction)
		print("Score: " + str(game.Score))
		if(game.GameWon):
			print("You win!")
			break

def pretty_print(board):
	for row in board:
		value_list = []
		for square in row:			
			value_list.append(square.value)
		print(value_list)


if __name__ == '__main__':
	main()