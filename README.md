boardList=[];
moves=[];


# See if anyone has won the game 
def hasWon(boardList):    
	X=['X','O']

	for i in range(0,1):
		if ((boardList[0]==boardList[4]==boardList[8]==X[i]) or (boardList[6]==boardList[4]==boardList[2]==X[i])):
			return True
		for index in range(0,3):
			if ((boardList[index]==boardList[index+1]==boardList[index+2]==X[i]) or (boardList[index]==boardList[index+3]==boardList[index+6]==X[i])):
			return True


#b(0),b(1),b(2)
#b(3),b(4),b(5)
#b(6),b(7),b(8)

print("Welcome to tic-tac-toe")

over = False;


def player1move():
	if (len(boardList)<=9):  # There is still moves left to be made
		amove = input("Enter a number from 0 through 8 to make your move")
		if (checkinput(amove) & amove not in moves):   # This move hasn't been taken, and is valid input
		moves.append(amove)  # Append the move to the moves list
		boardList[amove]='X' # Append the move to the boardlist
		if (hasWon(boardList)):
			print("Game Over")
			over = True;


def player2move():
	if (len(boardList)<=9):  # There is still moves left to be made
		amove = input("Enter a number from 0 through 8 to make your move")
		if (checkinput(amove) & amove not in moves):   # This move hasn't been taken, and is valid input
		moves.append(amove)  # Append the move to the moves list
		boardList[amove]='X' # Append the move to the boardlist
		displayboard()       # Display the board
		if (hasWon(boardList)):
			print("Game Over")
			over=True;


def playGame():
	while not over:
		player1move()
		player2move()

def checkinput(input):
	return (type(input)==int & (0<=input<=8))

def displayboard():
	print(boardList[0]+"|"+boardList[1]+"|"+boardList[2] \n 
		  boardlist[3]+"|"+boardlist[4]+"|"+boardList[5] \n
		  boardlist[6]+"|"+boardlist[7]+"|"+boardList[8])

