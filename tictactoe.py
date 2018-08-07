


boardList=[".",".",".",".",".",".",".",".","."]
moves=[]
over = False
count = 0


# See if anyone has won the game 
def hasWon(boardList):    
	X=['X','O']
	for i in range(0,1):
		if ((boardList[0]==boardList[4]==boardList[8]==X[i]) or (boardList[6]==boardList[4]==boardList[2]==X[i])):
			return True
		for index in range(0,2):
			if ((boardList[index*3]==boardList[index*3+1]==boardList[index*3+2]==X[i]) or (boardList[index]==boardList[index+3]==boardList[index+6]==X[i])):
				return True
		return False

# index=0===> b(0)=b(1)=b(2) or b(0)=b(3)=b(6)
# index=1===> b(3)=b(4)=b(5) or b(1)=b(4)=b(7)
# index=2===> b(6)=b(7)=b(8) or b(2)=b(5)=b(8)

#b(0),b(1),b(2)
#b(3),b(4),b(5)
#b(6),b(7),b(8)


def player1move():
	global count
	global displayboard
	global over
	global moves
	if (count == 9):
		print("Game Over, it was a tie")
		playAgain()
	if (count < 9):  # There is still moves left to be made
		count+=1  # Increment the counter, there will be 9 moves in the game.
		amove = input("Enter a number from 0 through 8 to make your move")
		amove = int(amove)
		while (amove in moves or checkinput(amove)==False):
			amove = input("Enter a number from 0 through 8 to make your move")
			amove = int(amove)

		if (checkinput(amove) and amove not in moves):
			moves.append(amove)  # Append the move to the moves list
			boardList[amove]='X' # Append the move to the boardlist
			displayboard()  # This move hasn't been taken, and is valid input

			if (hasWon(boardList)):
				print("Game Over")
				over = True;
				playAgain()

def player2move():
	global count
	global displayboard
	global over
	global moves
	if (count == 9):
		print("Game Over")
		playAgain()
	if (count < 9):  # There is still moves left to be made
		count+=1  # Increment the counter, there will be 9 moves in the game.

		amove = input("Enter a number from 0 through 8 to make your move")
		amove = int(amove)
		while (amove in moves or checkinput(amove)==False):
			amove = input("Enter a move not entered before or a valid number 0 through 8")
			amove = int(amove)

		if (checkinput(amove) and amove not in moves):   # This move hasn't been taken, and is valid input
			moves.append(amove)  # Append the move to the moves list
			boardList[amove]='O' # Append the move to the boardlist
			displayboard()

			if (hasWon(boardList)):
				print("Game Over")
				over=True;
				playAgain()


def playGame():
	while not over:
		player1move()
		player2move()
		print(boardList)

def checkinput(input):
	return (type(input)==int and (0<=input<=8))

def displayboard():
	print("\n \n")
	print(" " + boardList[0]+"|"+boardList[1]+"|"+boardList[2]+ "\n" +
		  " " + boardList[3]+"|"+boardList[4]+"|"+boardList[5]+ "\n" +
		  " " +boardList[6] +"|"+boardList[7]+"|"+boardList[8])
	print("\n \n")


def playAgain():
	global count
	global displayboard
	global over
	global moves
	inpu=""
	while(inpu != "Y" or inpu != "N"):
		inpu = input("Would you like to play Again? enter Y or N")
		if (inpu=="Y"):
			boardList=[".",".",".",".",".",".",".",".","."]
			moves=[]
			over = False
			count = 0
			playGame()
		if (inpu=="N"):
			quit()

playGame()


