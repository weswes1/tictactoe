boardList=[".",".",".",".",".",".",".",".","."]
moves=[]
over = False
count = 0


def hasWon(boardList):    
	X=['X','O']
	for i in range(0,1):
		if ((boardList[0]==boardList[4]==boardList[8]==X[i]) or (boardList[6]==boardList[4]==boardList[2]==X[i])):
			return True
		for index in range(0,2):
			if ((boardList[index*3]==boardList[index*3+1]==boardList[index*3+2]==X[i]) or (boardList[index]==boardList[index+3]==boardList[index+6]==X[i])):
				return True
	return False

def player1move():
	global over
	global count
	global boardlist
	global moves
	if (count == 9):
		print("Game Over. Tie")
		over = True
		return over
	if (count < 9):  # There is still moves left to be made
		count+=1  # Increment the counter, there will be 9 moves in the game.
		amove = input("Enter a number from 0 through 8 to make your move")
		amove = int(amove)
		while (amove in moves or checkinput(amove)==False):
			amove = input("A valid move not entered before")
			amove = int(amove)
		if (checkinput(amove) and amove not in moves):
			moves.append(amove)  # Append the move to the moves list
			boardList[amove]='X' # Append the move to the boardlist
			displayboard()  # This move hasn't been taken, and is valid input
			if (hasWon(boardList)):
				print("Game Over-")
				over = True
				return over

def player2move():
	global over
	global count
	global boardlist
	global moves
	if (count == 9):
		print("Game Over* Tie")
		over = True
		return over
	if (count < 9):  # There is still moves left to be made
		count+=1  # Increment the counter, there will be 9 moves in the game.
		amove = input("Enter a number from 0 through 8 to make your move")
		amove = int(amove)
		while (amove in moves or checkinput(amove)==False):
			amove = input("A valid move not entered before")
			amove = int(amove)

		if (checkinput(amove) and amove not in moves):   # This move hasn't been taken, and is valid input
			moves.append(amove)  # Append the move to the moves list
			boardList[amove]='O' # Append the move to the boardlist
			displayboard()

			if (hasWon(boardList)):
				print("Game Over***")
				over = True
				return over



def checkinput(input):
	return (type(input)==int and (0<=input<=8))

def displayboard():
	print("\n \n")
	print(" " + boardList[0]+"|"+boardList[1]+"|"+boardList[2]+ "\n" +
		  " " + boardList[3]+"|"+boardList[4]+"|"+boardList[5]+ "\n" +
		  " " +boardList[6] +"|"+boardList[7]+"|"+boardList[8])
	print("\n \n")

def getinput():
	inp=""
	while (inp!="y" or inp!="n"):
		inp=input("Enter y or n").lower()
		if(inp=="y"):
			return (inp=="y")
		if(inp=='n'):
			return (inp=="y")

while not over:
	player1move()
	if (over==True):
		if (getinput()):
			boardList=[".",".",".",".",".",".",".",".","."]
			moves=[]
			over = False
			count = 0
			continue
		else:
			quit()

	player2move()
	if (over==True):
		ins = input("Play again Y or N? ")
		if (getinput()):
			boardList=[".",".",".",".",".",".",".",".","."]
			moves=[]
			over = False
			count = 0
			continue
		else:
			quit()
