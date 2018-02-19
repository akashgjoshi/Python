##Simplified battle-ship game in python language

from random import randint
import getpass


def user_mode():
	user_mode=int(input("Choose 1 for single player and 2 for two player game: "))
	while True:
		if user_mode == 1 or user_mode == 2:
			True
			break
		else:
			print("Invalid user input. Please choose again.")
			False
			user_mode=int(input("Choose 1 for single player and  2 for two player game: "))
	return user_mode

def get_user_row():
	print("Let's hide the ship")
	user_row=int(getpass.getpass("Enter row. Enter row between 1 and 3 : "))
	while True:
		if user_row == 1 or user_row == 2 or user_row == 3:
			True
			break
		else:
			print("Invalid user input. Please choose again.")
			False
			user_row=int(getpass.getpass("Select row. Enter row between 1 and 3 : "))	
	return user_row	

def get_user_column():	
	user_column=int(getpass.getpass("Enter column. Enter row between 1 and 3 : "))
	while True:
		if user_column == 1 or user_column == 2 or user_column == 3:
			True
			break
		else:
			print("Invalid user input. Please choose again.")
			False
			user_column=int(getpass.getpass("Select column. Enter row between 1 and 3 : "))	
	return user_column	


def random_row(board):
    return randint(1, len(board) - 1)


def random_col(board):
    return randint(1, len(board[0]) - 1)
	

def print_board(board):
    for row in board:
        print(" ".join(row))

print("Let's play Battleship!")
		
user_mode=user_mode()

board = []
					
for x in range(3):
    board.append(["O"] * 3)	
										

if user_mode == 1:	
	ship_row = random_row(board)-1
	ship_col = random_col(board)-1
elif user_mode == 2:
	ship_row=get_user_row() -1
	ship_col = get_user_column() -1 

print("------------------------------------------------------")	
print("Select values between 1 and 3(inclusive) for both, row and column to find the BattleShip")
print("You have 3 chances")
print_board(board)	

for turn in range(3):
    guess_row = int(input("Guess Row:"))-1
    guess_col = int(input("Guess Col:"))-1

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean. Please try with values between 1 and 3")
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        print (turn + 1)
        print_board(board)
        if turn>2:
            print("Game Over")

print("The ship location is Row:%d  and Column: %d"%(ship_row+1,ship_col+1))
board[ship_row][ship_col] = "S"
print_board(board)       
    
 