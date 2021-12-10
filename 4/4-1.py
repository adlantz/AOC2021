import numpy as np

inputList = open("4.txt", "r").readlines()


# get list of bingo numbers as list of ints
bingoNumbers = list(map(int,inputList[0][:-1].split(',')))

#put all bingo boards into 3D array (an array of 2d bingo boards)
bingoBoards = inputList[2:]
boardMatrix = []
board = []
for i in range(len(bingoBoards)):
  if bingoBoards[i] == '\n':
    boardMatrix.append(board)
    board = []
    continue
  else:
    board.append(list(map(int," ".join(bingoBoards[i][:-1].split()).split(' '))))

#create a list of cols and rows of each board where each col and row is a python set
boardSetMatrix = []
for board in boardMatrix:
  boardSetList = []
  for row in board:
    boardSetList.append(set(row))

  for col in np.transpose(board):
    boardSetList.append(set(col))
  boardSetMatrix.append(boardSetList)

#keep expanding number of bingo numbers to look at until a row or column is complete
bingo = False
n = 5
while not bingo:
  numberSet = set(bingoNumbers[:n])
  for i in range(len(boardSetMatrix)):
    boardSetList = boardSetMatrix[i]
    for boardSet in boardSetList:
      if boardSet.issubset(numberSet):
        bingo = True
        break
    if bingo:
      break
  n+=1

lastNumCalled = bingoNumbers[n-2]
notCalled = set(np.array(boardMatrix[i]).flatten()).difference(numberSet)
print(sum(notCalled) * lastNumCalled)


