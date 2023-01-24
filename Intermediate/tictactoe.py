
 # "Storage" for tic tac toe board
 ttt_board = []

void main():
	
	# Starting player holding value
	st_pl = 'NONE'
	# Welcomes user, returns starting player
	welcome_msg()
	rc_select()

# Function to welcome the user when called	
# INPUT: Nothing, user input
# OUTPUT: starting_player
def welcome_msg():
	# Array containing possible user choices
	users = ["X", "O"]
	display_value = [0,1,2,3,4,5,6,7,8]
	clear_value = [0,0,0,0,0,0,0,0,0]
	rc_display_value = ["[0,0]","[0,1]", "[0,2]", "[1,0]", "[1,1]", "[1,2]", "[2,0]", "[2,1]", "[2,2]"]
	user_choice = False
	
	# Welcome message
	print("Welcome to Tic Tac Toe!" + "\n" + "How to play: Choose X or O, and score three in a row!")
	print("Take a look at the board below. To play, you will enter a row (0-2), and then a column (0-2) to put your symbol.")
	print("For example, to get an X or O where the 0 is, answer row 0, and column 0. To get an X or O where the 8 is, answer row 2, and column 2.")
	print_tic_tac_toe(display_value)
	ans = input("Sound good? Answer Y to proceed, or N for a list of possible combinations:")
	if ans is "Y" or "N":
		if ans == "Y":
			pass
		elif ans == "N":
			print("No? Here is the board with the row and column combinations in [row, column] format: ")
			print_tic_tac_toe(rc_display_value)
	else:
		print("Sorry, I did not quite get that. Proceeding.")
	# Keep running the while loop until user_choice is set to true
	while user_choice == False:
		starting_player = input("Do you want to play? Type X or O to decide who starts first: ")
		if starting_player in users:
			print("Great!" + starting_player + " starts first!")
			user_choice = True
		else:
			print("Sorry, I did not understand that. Please type X or O.")
			user_choice = False
	
	# "Clear" the board and display
	print("Here is a brand new board: \n")
	print_tic_tac_toe(clear_value)
	return starting_player

# Function to print Tic Tac Toe
# INPUT: global ttt_board array
# OUTPUT: nothing, prints entire board to display
def print_tic_tac_toe(ttt_board):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(ttt_board[0], ttt_board[1], ttt_board[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(ttt_board[3], ttt_board[4], ttt_board[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(ttt_board[6], ttt_board[7], ttt_board[8]))
    print("\t     |     |")
    print("\n")

# Function to allow the user to select the row, column, then validate if the space already has an input
# INPUT: nothing, user input
# OUTPUT: choice(row, column)
def rc_select():

	# value to translate for translation table
	combo_choice = str(choice[0] + choice[1])

	# Runs sel and pastes to 
	translation_table(combo_choice)
	
	# Translation table
	# choice[0,0] = ttt[0], choice[0,1] = ttt[1], choice[0,2] = ttt[2]
	# choice[1,0] = ttt[3], choice[1,1] = ttt[4], choice[1,2] = ttt[5]
	# choice[2,0] = ttt[6], choice[2,1] = ttt[7], choice[2,2] = ttt[8]
	translation_table = {
		'00': select(ttt_board[0]),
		'01': select(ttt_board[1]),
		'02': select(ttt_board[2]),
		'10': select(ttt_board[3]),
		'11': select(ttt_board[4]),
		'12': select(ttt_board[5]),
		'20': select(ttt_board[6]),
		'21': select(ttt_board[7]),
		'22': select(ttt_board[8]),
	}
	
	# Run a loop 9 times, 0-8, ask players for input each time
	# User inputs row and column
	# Program validates selection and verifies if selected space is clear for input
	for i in range(8):

		# Values to validate numeric choice
		choice = []
		acceptable_values = [0,1,2]
		within_range = False
		
		# Check two conditions:
		# Is our row a digit or within_range == False
		while choice.isdigit() == False or within_range == False:
			# Ask for the row
			choice[0] = input("Please enter the row (0,1, or 2): ")
			# Verify that the input is a digit then verify if its within the range of 0-2
			if choice[0].isdigit() == False:
				print("Sorry, that is not a digit, try again!")
			if choice[0].isdigit() == True:
				if choice in acceptable_values:
					within_range = True
				else:
					print("Sorry, you are not within the acceptable range (0-2). Try again.")
					within_range = False
			# Ask for the column
			choice[1] = input("Please enter the column (0,1, or 2): ")
			# Verify that the input is a digit then verify its range is 0-2
			if choice[1].isdigit() == False:
				print("Sorry, that is not a digit, try again!")
			if choice[1].isdigit() == True:
				if choice in acceptable_values:
					within_range = True
				else:
					print("Sorry, you are not within the acceptable range (0-2). Try again.")
					within_range = False

	# Verify that an item is not already there, maybe ask global function that translates 0-9 into row x column

	
	return int(choice)
# Verify if we should be allowed to place the users symbol there
def select(some_array_index):
	
	# If array is not occupied by X or O, proceed
	if 'X' or 'O' not in some_array_index:

	else:
		print("Occupied by an X or O already.")
		return
