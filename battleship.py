
#imports
import random, os, time

#parameters
numRows=10
numCols=10
shipLength=4
shipSpace=6
correct=0
count=0
board=[]
hiddenBoard=[]

#creating the board
for r in range(numRows):
	rowList=[]
	for c in range(numCols):
		rowList.append(' ')

	board.append(rowList)

#printing the board
for c in range(numCols):
	print('   '+str(c)+' ',end=' ')	
print()
for r in range(numRows):
    print(r,' ',end=' ')
    for c in range(numCols):
    	print(board[r][c]+'  |  ', end='')
    print('\n ','-----+'*numCols)
print()

#creating the hidden board
for r in range(numRows):
	rowList=[]
	for c in range(numCols):
		rowList.append(' ')

	hiddenBoard.append(rowList)

#game introduction
print('This is BATTLESHIP!')
time.sleep(0.5)
print('Try to hit the ship and win!!')
time.sleep(0.5)

#ship position
shipPosition=random.randint(0,1)
randomRow=random.randint(0,numRows-4)
randomCol=random.randint(0,numCols-4)
hiddenBoard[randomRow][randomCol]='X'

#ship orientation
for a in range(shipLength):
	if shipPosition==0: #horizontal
		hiddenBoard[randomRow][randomCol+a]='X'
	
	elif shipPosition==1: #vertical
		hiddenBoard[randomRow+a][randomCol]='X'

#printing hidden board
#for c in range(numCols):
	#print('   '+str(c)+' ',end=' ')	
#print()
#for r in range(numRows):
    #print(r,' ',end=' ')
    #for c in range(numCols):
    	#print(hiddenBoard[r][c]+'  |  ', end='')
    #print('\n ','-----+'*numCols)
#print()

#using the loop to check and compare the inputs
#print(randomRow, randomCol)
check='TRUE'
while check=='TRUE':
	print('Number of tries: ',count)
	
	#user's inputs
	rowGuess=int(input('Choose the row (integer): '))
	colGuess=int(input('Choose the column (integer): '))
	#validation 
	if rowGuess>9 or colGuess>9 or rowGuess<0 or colGuess<0 or rowGuess==' ' or colGuess==' ':
		print ('The number you chose is out of range.')
		time.sleep(0.5)
		print('Enter a valid integer between 0 and 9.')
		count=count+1
	
	elif hiddenBoard[rowGuess][colGuess] == ' ':
		os.system('clear')
		board[rowGuess][colGuess]='o'

		for c in range(numCols):
			print('   '+str(c)+' ',end=' ')	
		print()
		for r in range(numRows):
			print(r,' ',end=' ')
			for c in range(numCols):
				print(board[r][c]+'  |  ', end='')
			print('\n ','-----+'*numCols)
		print()
         
		print ('Ooops. Wrong guess! ')
		
		count=count+1
	elif hiddenBoard[rowGuess][colGuess] == 'X':
		os.system('clear')
		board[rowGuess][colGuess] = 'x'
		count=count+1

		for c in range(numCols):
			print('   '+str(c)+' ',end=' ')	
		print()
		for r in range(numRows):
			print(r,' ',end=' ')
			for c in range(numCols):
				print(board[r][c]+'  |  ', end='')
			print('\n '+'-----+'*numCols)
		print()

		print ('You got it!!!')
		time.sleep(0.5)
		print("IT'S A HIT!!!")
		print('Keep going! ')
		os.system('clear')

		correct=correct+1   
		
	if (correct == shipLength):
		check='FALSE' 
	

print('YOU DID IT!!')
time.sleep(1)
print('You did it in',count,'tries.')
print('GREAT JOB!')
time.sleep(0.5)
print('YOU WON THIS BATTLE!')
time.sleep(1)
print('Maybe just because you are lucky......')


