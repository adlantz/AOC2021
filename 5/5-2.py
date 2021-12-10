import numpy as np
inputList = open("5.txt", "r").readlines()

pntslist = []
for line in inputList:
  splitline = line[:-1].split(" ")
  p1 = tuple((int(splitline[0].split(',')[0]),int(splitline[0].split(',')[1])))
  p2 = tuple((int(splitline[-1].split(',')[0]),int(splitline[-1].split(',')[1])))
  if(p1[0] == p2[0]):
    for i in range(min(p1[1],p2[1]),max(p1[1],p2[1])+1):
      pntslist.append((p1[0],i))
  elif p1[1] == p2[1]:
    for i in range(min(p1[0],p2[0]),max(p1[0],p2[0])+1):
      pntslist.append((i,p1[1]))
  else:
    orderx = -1 if p1[0]>p2[0] else 1
    lx = [x for x in range(p1[0],p2[0]+orderx,orderx)]
    ordery = -1 if p1[1]>p2[1] else 1
    ly = [y for y in range(p1[1],p2[1]+ordery,ordery)]
    for i in range(len(lx)):
      pntslist.append((lx[i],ly[i]))


coordsMatrix = np.zeros((999,999))

for t in pntslist:
  coordsMatrix[t[0]][t[1]] +=1

dups=0
for c in coordsMatrix.flatten():
  if c>1:
    dups+=1

print(dups)