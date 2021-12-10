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

boardIndexSet = set([i for i in range(len(boardMatrix))])

#remove boards as they are bingo'd and keep track of the last one removed
n=5
lastRemoved=99999
while(len(boardIndexSet) > 0):
  numberSet = set(bingoNumbers[:n])
  iRemoveSet = set()
  for i in boardIndexSet:
    boardSetList = boardSetMatrix[i]
    for boardSet in boardSetList:
      if boardSet.issubset(numberSet):
        iRemoveSet.add(i)
        lastRemoved = i
        break
  for index in iRemoveSet:
    boardIndexSet.remove(index)
  n+=1

lastNumCalled = bingoNumbers[n-2]
notCalled = set(np.array(boardMatrix[lastRemoved]).flatten()).difference(numberSet)
print(sum(notCalled) * lastNumCalled)



