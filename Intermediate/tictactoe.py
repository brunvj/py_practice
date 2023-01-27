
  # "Storage" for tic tac toe board
 ttt_board = []

void main():
	player1 = ""
	player2 = ""
	# Starting player holding value
	# Welcomes user, returns starting player
	welcome_msg(player1,player2)
	
	# Lets starting player start the game, selecting a row and column, validating, verifying, displaying selections, and after
	# 6 turns, checks the board for winner and loser or tie.
	rc_select(player1, player2)

# Function to welcome the user when called	
# INPUT: Nothing, user input
# OUTPUT: starting_player
def welcome_msg(first_player, second_player):
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
		first_player = input("Do you want to play? Type X or O to decide who starts first: ")
		if first_player in users:
			print("Great!" + first_player + " starts first!")
			if first_player == "X":
				second_player = "O"
			else:
				second_player = "X"
			user_choice = True
		else:
			print("Sorry, I did not understand that. Please type X or O.")
			user_choice = False
	
	# "Clear" the board and display
	print("Here is a brand new board: \n")
	print_tic_tac_toe(clear_value)
	return first_player, second_player

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
# INPUT: players 1 and 2
# OUTPUT: choice(row, column)
def rc_select(players1, players2):

	# value to translate for translation table
	combo_choice = str(choice[0] + choice[1])
	# value to tell rc_select that we are letting players1 go first
	player = players1
	# value to hold turns count
	count = 0
	
	# initializing tuple value
	three = tuple()
	# Translation table
	# choice[0,0] = ttt[0], choice[0,1] = ttt[1], choice[0,2] = ttt[2]
	# choice[1,0] = ttt[3], choice[1,1] = ttt[4], choice[1,2] = ttt[5]
	# choice[2,0] = ttt[6], choice[2,1] = ttt[7], choice[2,2] = ttt[8]
	translation_table = {
		'00': select(ttt_board[0], player),
		'01': select(ttt_board[1], player),
		'02': select(ttt_board[2], player),
		'10': select(ttt_board[3], player),
		'11': select(ttt_board[4], player),
		'12': select(ttt_board[5], player),
		'20': select(ttt_board[6], player),
		'21': select(ttt_board[7], player),
		'22': select(ttt_board[8], player),
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
		# Is our row,column a digit or within_range == False
		while choice[0].isdigit() or choice[1].isdigit() == False or within_range == False:
			# Ask for the row
			choice[0] = input("Please enter the row (0,1, or 2): ")
			# Ask for the column
			choice[1] = input("Please enter the column (0,1, or 2): ")
			# Verify that the input is a digit then verify if its within the range of 0-2
			if choice[0].isdigit() and choice[1].isdigit() == False :
				print("Sorry, you did not enter a valid digit for the row and/or column, try again!")
				choice.isdigit == False
			
			elif choice[0].isdigit() and choice[1].isdigit() == True:
				# If our choices are digits, lets see if they are in the acceptable choices list
				if choice[0] and choice[1] in acceptable_values:
					within_range = True
					# Our choices are valid digits, and are in the acceptable choices list, now proceed to check if the space is occupied
					if translation_table{combo_choice, player} == True:
						print("Great, here is the board with your updated input: ")
						print_tic_tac_toe()
						# Now switch player
						if player == players1:
							player = players2
						else:
							player = players1

						print("Now, " + player + ", it is your turn!")
					else:
						print("Sorry, it looks like there is a symbol already at the location you selected.")
						within_range = False
				else:
					print("Sorry, one or both of your choices are not within the acceptable range (0-2). Try again.")
					within_range = False
		# When we near the end of the while loop validation, it means the inputs were correct, so next:
		# 1. Check if the space is occupied
		# 2. Check if we have 6 turns, and find out if we have a winner
		# 3. When finished with each for loop iteration, change the player

		# If we're at the 6th turn, we can start validating the winner using the board_checker function
		if count >= 5:
			three = board_checker()
			
			count += 1
		# If count is less than 5, lets add 1 to count and start the next
		else:
			pass
			count += 1
	
	return int(choice)

# Verify if we should be allowed to place the users symbol there
# INPUT: array_index, player, chosen by translator dictionary
# OUTPUT: bool value, to show rc_select we either placed the symbol in its spot or did not
def select(array_index, i_player):
	
	# If array is not occupied by X or O, assign the array_index value to the string "X" or "O" (ttt_board[5] = "O")
	if 'X' or 'O' != array_index:
		array_index = str(i_player)
		return True

	# If array is occupied by X or O, do nothing except return false
	else:
		return False


# Checks if global board has any horizontals or diagonals and declares win, tie, or loss
# INPUT: ttt_board
# OUTPUT: tuple (true, winner, loser), (true, tie, tie), (true, loser, winner), (false, null, null)
def board_checker(ttt_board, player1, player2):

	decider = (bool winner, str player1, str player2)
	if ttt_board[0] and ttt_board[1] and ttt_board[2] == player1 or player2:
		winner = True
	if ttt_board[3] and ttt_board[4] and ttt_board[5] == player1 or player2:
		winner = True
	if ttt_board[6] and ttt_board[7] and ttt_board[8] == player1 or player2:
		winner = True
	if ttt_board[0] and ttt_board[4] and ttt_board[8] == player1 or player2:
		winner = True
	if ttt_board[6] and ttt_board[4] and ttt_board[2] == player1 or player2:
		winner = True
	if ttt_board[0] and ttt_board[3] and ttt_board[6] == player1 or player2:
		winner = True
	if ttt_board[1] and ttt_board[4] and ttt_board[7] == player1 or player2:
		winner = True
	if ttt_board[2] and ttt_board[5] and ttt_board[8] == player1 or player2:
		winner = True
